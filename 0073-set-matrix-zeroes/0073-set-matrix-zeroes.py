class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        def makeZero(row, col):
            for i in range(rows):
                matrix[i][col] = 0
            for i in range(cols):
                matrix[row][i] = 0
        
        zeros = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        for l in zeros:
            makeZero(l[0], l[1])