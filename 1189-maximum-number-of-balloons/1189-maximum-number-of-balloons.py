class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for i in text:
            if i in balloon:
                balloon[i] += 1
        
        res = 100000000000
        for i in balloon:
            if i == "b":
                res = min(res, balloon[i])
            elif i == "a":
                res = min(res, balloon[i])
            elif i == "l":
                res = min(res, balloon[i]//2)
            elif i == "o":
                res = min(res, balloon[i]//2)
            else:
                res = min(res, balloon[i])
        
        return res
        