class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        n = min(len(num1), len(num2))
        
        res = ""
        remain = 0
        for i in range(n):
            p = int(num1[i]) + int(num2[i]) + int(remain)
            if p >= 10:
                p = str(p)
                remain = p[0]
                res += p[1]
            else:
                res += str(p)
                remain = 0
        
        if len(num1) > len(num2):
            for i in range(n, len(num1)):
                p = int(num1[i]) + int(remain)
                if p >= 10:
                    p = str(p)
                    remain = p[0]
                    res += p[1]
                else:
                    res += str(p)
                    remain = 0
            if int(remain) != 0:
                res += remain

        elif len(num1) < len(num2):
            for i in range(n, len(num2)):
                p = int(num2[i]) + int(remain)
                if p >= 10:
                    p = str(p)
                    remain = p[0]
                    res += p[1]
                else:
                    res += str(p)
                    remain = 0
            if int(remain) != 0:
                res += remain
        
        else:
            if int(remain) != 0:
                res += remain
        
        return res[::-1]



        