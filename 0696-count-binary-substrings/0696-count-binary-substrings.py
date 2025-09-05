class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('01', '0 1').replace('10', '1 0').split(" ")
        res = 0

        for i in range(1,len(s)):
            res += min(len(s[i]), len(s[i-1]))
        
        return res
        