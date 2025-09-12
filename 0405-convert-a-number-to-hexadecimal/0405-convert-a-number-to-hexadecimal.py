class Solution:
    def toHex(self, num: int) -> str:
        if num >= 0:
            return hex(num)[2:]
        
        num = bin(num)[3:]
        
        temp = ""
        for _ in range(32-len(num)):
            temp += "0"
        
        num = temp + num
        temp = ""
        for i in num:
            if i == '0':
                temp += '1'
            else:
                temp += '0'

        temp = int(temp, 2)
        temp += 1
        
        return hex(temp)[2:]
        