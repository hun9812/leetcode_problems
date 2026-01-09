class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        appear = {}
        check = -1
        res = 0
        for i in range(len(s)):
            cur = s[i]
            if cur not in appear:
                appear[cur] = -1
            res = max(res, i - max(check, appear[cur]))
            if appear[cur] != -1:
                check = max(appear[cur], check)
            appear[cur] = i
            # print(cur, appear, res, check)

        return res 