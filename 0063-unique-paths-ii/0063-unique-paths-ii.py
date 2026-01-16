class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                res[i][0] = 0
            else:
                res[i][0] = res[i-1][0]
        
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                res[0][i] = 0
            else:
                res[0][i] = res[0][i-1]



        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[m-1][n-1]
        
        