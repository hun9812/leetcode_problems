class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rev = True

        res = ""
        
        cur = 0
        while cur+k <= len(s):
            if rev:
                res += s[cur:cur+k][::-1]
                rev = False
                cur += k
            else:
                res += s[cur:cur+k]
                rev = True
                cur += k
        
        if rev:
            res += s[cur:][::-1]
        else:
            res += s[cur:]
        
        return res
        