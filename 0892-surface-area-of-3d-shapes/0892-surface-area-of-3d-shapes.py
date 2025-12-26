class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        res = 0
        move = [[-1,0], [1,0], [0,-1], [0,1]]
        for i in range(len(grid)):
            for j in range(len(grid)):
                for k in move:
                    check_i = i + k[0]
                    check_j = j + k[1]
                    if check_i < 0 or check_i >=n:
                        res += grid[i][j]
                        continue
                    if check_j<0 or check_j>=n:
                        res += grid[i][j]
                        continue
                    if grid[i][j] > grid[check_i][check_j]:
                        res += grid[i][j] - grid[check_i][check_j]
                    
                if grid[i][j] != 0:
                    res += 2
        return res
