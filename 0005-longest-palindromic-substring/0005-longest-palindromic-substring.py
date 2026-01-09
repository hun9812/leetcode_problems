class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        # res = 1
        res_str = s[0]
        for i in range(1, len(s)):
            temp1 = 1
            temp2 = 2
            for j in range(1, i+1):
                try:
                    if s[i-j] == s[i+j]:
                        temp1 += 2
                    else:
                        break
                except:
                    break
            if s[i] == s[i-1]:    
                for j in range(1, i):
                    try:
                        if s[i+j] == s[i-1-j]:
                            temp2 += 2
                        else:
                            break
                    except:
                        break
            else:
                temp2 = 0
            
            #print(i, temp1, temp2, res, res_str)

            if temp1 > len(res_str) and temp1 > temp2:
                res_str = s[i-(temp1//2): i+1+(temp1//2)]
            
            elif temp2 > len(res_str) and temp2 > temp1:
                res_str = s[i-(temp2//2) : i+(temp2//2)]

        return res_str
        