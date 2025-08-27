class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        row = len(grid)
        column = len(grid[0])
        res = 0
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0:
                    continue
                for k in range(4):
                    check = [i+move[k][0], j+move[k][1]]
                    if check[0] < 0 or check[1] < 0:
                        res += 1
                        continue
                    try:
                        if grid[check[0]][check[1]] == 0:
                            res +=1
                            # print(check[0], check[1])
                    except:
                        res += 1
                        # print("Except", check[0], check[1])
         
        return res

        