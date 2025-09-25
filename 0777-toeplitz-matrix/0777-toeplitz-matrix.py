class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        self.matrix = matrix
        for i in range(len(self.matrix)):
            if self.checkdiagonal(i, 0) == False:
                return False
        
        for i in range(len(self.matrix[0])):
            if self.checkdiagonal(0, i) == False:
                return False
        
        return True
    

    def checkdiagonal(self, row, col):
        cur = self.matrix[row][col]
        while True:
            try:
                row += 1
                col += 1
                if self.matrix[row][col] != cur:
                    return False
            except:
                return True
        