class Solution:
    def myAtoi(self, s: str) -> int:
        isnum = "0123456789"
        negative = False
        positive = False
        res = ""
        for i in range(len(s)):
            if s[i] in isnum:
                zero = False
                if s[i] == "0":
                    zero = True
                while True:
                    if zero:
                        if s[i] == "0":
                            i += 1
                            if  i>=len(s) or s[i] not in isnum:
                                return 0
                            continue
                        else:
                            zero = False
                    res += s[i]
                    i += 1
                    if  i >= len(s) or s[i] not in isnum:
                        break
                if negative:
                    res = "-" + res
                    inlimit = self.check(res)
                    if inlimit:
                        return int(res)
                    else:
                        return -(2**31)
                else:
                    inlimit = self.check(res)
                    # print(inlimit, res)
                    if inlimit:
                        return int(res)
                    else:
                        return (2**31)-1                
            elif s[i] == "-":
                if positive or negative:
                    break
                negative = True
            elif s[i] == "+":
                if positive or negative:
                    break
                positive = True
            elif s[i] == " ":
                if positive or negative:
                    break
                continue
            else:
                break
        return 0


    def check(self, x):
        if x[0] != "-":
            temp = 2**31 - 1
            temp = str(temp)
            if len(temp) > len(x):
                return True
            if len(temp) < len(x):
                return False
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
            if len(temp) < len(x):
                return False
            for i in range(1,len(x)):
                if int(x[i]) > int(temp[i]):
                    return False
                elif int(x[i]) < int(temp[i]):
                    return True
                else:
                    continue        
            return True
        