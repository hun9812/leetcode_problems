class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = [0,0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    rook_pos = [i,j]
                    break
            if rook_pos != [0,0]:
                break
        
        count = 0
        for u in range(rook_pos[0]+1, len(board)):
            if board[u][rook_pos[1]] == ".":
                continue
            elif board[u][rook_pos[1]] == "p":
                count += 1
                break
            else:
                break

        for u in range(rook_pos[0]-1, -1, -1):
            if board[u][rook_pos[1]] == ".":
                continue
            elif board[u][rook_pos[1]] == "p":
                count += 1
                break
            else:
                break
        
        for u in range(rook_pos[1]+1, len(board[0])):
            if board[rook_pos[0]][u] == ".":
                continue
            elif board[rook_pos[0]][u] == "p":
                count += 1
                break
            else:
                break
        
        for u in range(rook_pos[1]-1, -1,-1):
            if board[rook_pos[0]][u] == ".":
                continue
            elif board[rook_pos[0]][u] == "p":
                count += 1
                break
            else:
                break
        return count
        