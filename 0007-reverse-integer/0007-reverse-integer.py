class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            checked = self.check(x)
            if not checked:
                return 0
        else:
            x = str(x)
            x = x[1:]
            x = "-" + x[::-1]
            checked = self.check(x)
            if not checked:
                return 0
        
        return int(x)
    
    def check(self, x):
        if x[0] != "-":
            temp = 2**31 - 1
            temp = str(temp)
            if len(temp) > len(x):
                return True
            for i in range(len(x)):
                if int(x[i]) > int(temp[i]):
                    return False
                elif int(x[i]) < int(temp[i]):
                    return True
                else:
                    continue
            return True
        else:
            temp = -(2**31)
            temp = str(temp)
            if len(temp) > len(x):
                return True
            for i in range(1,len(x)):
                if int(x[i]) > int(temp[i]):
                    return False
                elif int(x[i]) < int(temp[i]):
                    return True
                else:
                    continue        
            return True