class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = 1
        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                res = 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j]**2)
        
        return res
        
        
        
        
        # self.res = 0
        
        # def one_matrix(m, n):
        #     if m*n <= self.res:
        #         return
        #     for i in range(0, len(matrix)-m+1):
        #         for j in range(0, len(matrix[0])-n+1):
        #             # check
        #             check = False
        #             for u in range(m):
        #                 for v in range(n):
        #                     if matrix[i+u][j+v] != "1":
        #                         check = True
        #                 if check == True:
        #                     break
        #             if check == False:
        #                 print(i,j, m, n)
        #                 self.res = m*n
        #                 return
        
        # for m in range(len(matrix), 0, -1):
        #     #for n in range(len(matrix[0]), 0, -1):
        #     one_matrix(m,m)

        # return self.res