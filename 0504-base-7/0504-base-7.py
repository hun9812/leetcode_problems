class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = False
        if num < 0:
            neg = True
        num = abs(num)

        if num == 0:
           return "0"

        res = ""

        while num:
            res += str(num % 7)
            num //= 7
        
        res = res[::-1]

        if neg:
            return '-' + res
        else:
            return res