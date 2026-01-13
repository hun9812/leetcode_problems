class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            appear = [False for _ in range(10)]
            for j in i:
                if j == '.':
                    continue
                check = int(j)
                if appear[check] == True:
                    return False
                else:
                    appear[check] = True
        
        for columns in range(9):
            appear = [False for _ in range(10)]
            for rows in range(9):
                check = board[rows][columns]
                if check == '.':
                    continue
                check = int(check)
                if appear[check] == True:
                    return False
                else:
                    appear[check] = True
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                appear = [False for _ in range(10)]
                for u in range(3):
                    for v in range(3):
                        check = board[i+u][j+v]
                        if check == '.':
                            continue
                        check = int(check)
                        if appear[check] == True:
                            return False
                        else:
                            appear[check] = True
        
        return True

        