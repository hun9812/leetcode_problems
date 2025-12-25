class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        col = 0
        row = 0
        for i in grid:
            row += max(i)
            for j in i:
                if j != 0:
                    top += 1
        
        for i in range(len(grid[0])):
            cur = 0
            for j in range(len(grid)):
                cur = max(cur, grid[j][i])
            col += cur
        # print(col, row, top)
        return col+row+top

        