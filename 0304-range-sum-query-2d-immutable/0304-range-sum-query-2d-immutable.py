class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat_cal = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            self.mat_cal[i][0] = matrix[i][0]
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.mat_cal[i][j] = self.mat_cal[i][j-1] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                res += self.mat_cal[i][col2]
            else:
                res += (self.mat_cal[i][col2] - self.mat_cal[i][col1-1])
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)