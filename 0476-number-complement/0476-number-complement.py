class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
    
        res = "0b"
        check = True
        for i in num:
            if i == '0':
                check = False
                res += '1'
            else:
                if check == True:
                    continue
                res += '0'
                
        if res == '0b':
            return 0

        res = int(res, 2)
        
        return res