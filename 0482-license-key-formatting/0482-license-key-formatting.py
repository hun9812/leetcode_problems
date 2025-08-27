class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        cur = 0
        res = ''
        for i in s:
            if i == "-":
                continue
            elif i.isdigit():
                res += i
            else:
                res += i.upper()
            cur += 1
            if cur == k:
                res += '-'
                cur = 0
        
        res = res[::-1]
        if len(res) == 0:
            return res
        if res[0] == '-':
            res = res[1:]
        return res
        