class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        res[0][0] = 1

        cur = 2
        u,v = 0,0
        p_move = 0
        move = [[0,1], [1,0], [0,-1], [-1,0]]
        for _ in range(n*n-1):
            for _ in range(4):
                check_u, check_v = u+move[p_move][0], v+move[p_move][1]
                if check_u >= n or check_v >= n:
                    p_move = (p_move + 1) % 4
                elif check_u < 0 or check_v < 0:
                    p_move = (p_move + 1) % 4
                elif res[check_u][check_v] != 0:
                    p_move = (p_move + 1) % 4
                else:
                    u = check_u
                    v = check_v
                    res[u][v] = cur
                    cur += 1
                    break
        return res