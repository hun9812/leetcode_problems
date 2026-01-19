class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        move = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = [[False for _ in range(n)] for _ in range(m)]

        def search(cur_m, cur_n, cur_word):
            if len(cur_word) == 0:
                return True
            res = False
            for i in move:
                check_m = cur_m + i[0]
                check_n = cur_n + i[1]
                if check_m < 0 or check_m >= m:
                    continue
                if check_n < 0 or check_n >= n:
                    continue
                if board[check_m][check_n] != cur_word[0]:
                    continue
                if visited[check_m][check_n] == True:
                    continue
                if len(cur_word) == 1:
                    return True
                else:
                    visited[check_m][check_n] = True
                    res = res or search(check_m, check_n, cur_word[1:])
                    visited[check_m][check_n] = False
            return res
        
        for i in range(m):
            for j in range(n):
                visited = [[False for _ in range(n)] for _ in range(m)]
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if len(word) == 1:
                        return True
                    output = search(i,j,word[1:])
                    if output == True:
                        return True
                else:
                    continue
        return False