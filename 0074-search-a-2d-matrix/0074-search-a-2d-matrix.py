class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        
        if m == 1 or matrix[-1][0] <= target:
            row = m-1
        else:
            start = 0
            end = m-1
            while start <= end:
                mid = (start + end) // 2
                if matrix[mid][0] <= target and matrix[mid+1][0] > target:
                    row = mid
                    break
                if matrix[mid][0] > target:
                    end = mid-1
                else:
                    start = mid+1
        col = -1
        start = 0
        end = n-1
        while start <= end:
            mid = (start+end) // 2
            if matrix[row][mid] == target:
                col = mid
            if matrix[row][mid] > target:
                end = mid -1
            else:
                start = mid + 1
        print(row, col)
        if col != -1:
            return True
        else:
            return False
