class Solution:
    def numDecodings(self, s: str) -> int:
        
        res = [0 for _ in range(len(s))]
       
        if s[0] == "0":
            return 0
        else:
            res[0] = 1
        
        if len(s) == 1:
            return 1
        else:
            if int(s[0:2]) >= 10 and int(s[0:2]) <= 26:
                if s[1] != "0":
                    res[1] = 2
                else:
                    res[1] = 1
            else:
                if s[1] != "0":
                    res[1] = 1
                else:
                    return 0

        for i in range(2, len(s)):
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    res[i] = res[i-2]
                else:
                    return 0
            else:
                if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                    res[i] = res[i-1]+res[i-2]
                else:
                    res[i] = res[i-1]
        
        return res[-1]        
        
        # self.res = 0

        # def decode(i):
        #     # print(i)
        #     if i == len(s):
        #         self.res += 1
        #         return
        #     if s[i] != str(0):
        #         decode(i+1)
        #     if i+1 <= len(s)-1:
        #         if int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
        #             decode(i+2)
        
        # decode(0)
        # return self.res