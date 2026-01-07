class Solution:
    def divisorGame(self, n: int) -> bool:
        
        res = [True, False, True, False]
        for i in range(4, n+1):
            check = False
            for j in range(1,n//2+1):
                if i % j == 0:
                    if res[i-j] == False:
                        res.append(True)
                        check = True
                        break
            if not check:
                res.append(False)
        
        return res[n]

        