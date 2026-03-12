class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = 0
        col_num = len(matrix[0])-1

        while row_num < len(matrix) and col_num >= 0:
            cur = matrix[row_num][col_num]
            if cur == target:
                return True
            elif cur < target:
                row_num += 1
            else:
                col_num -= 1
        
        return False