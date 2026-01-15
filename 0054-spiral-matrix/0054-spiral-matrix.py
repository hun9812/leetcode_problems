class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        prev_move = 0
        move = [[0,1], [1,0], [0,-1], [-1,0]]

        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        u,v = 0,0
        visited[0][0] = True
        res = [matrix[0][0]]
        for _ in range((len(matrix) * len(matrix[0])) - 1):
            # print(visited)
            for _ in range(4):
                cur_move = move[prev_move]
                print(u+cur_move[0], v+cur_move[1])
                if (
                    u+cur_move[0] >= 0 and u+cur_move[0] < len(matrix) and 
                    v+cur_move[1] >= 0 and v+cur_move[1] < len(matrix[0]) and 
                    visited[u+cur_move[0]][v+cur_move[1]] != True
                ):

                   u = u+cur_move[0]
                   v = v+cur_move[1]
                   res.append(matrix[u][v])
                   visited[u][v] = True
                   # print("did",u,v)
                   break
                else:
                    prev_move += 1
                    prev_move %= 4
        
        return res