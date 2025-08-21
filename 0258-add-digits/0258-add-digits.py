class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            temp = 0
            for i in num:
                temp += int(i)
            num = str(temp)
            
        return int(num)