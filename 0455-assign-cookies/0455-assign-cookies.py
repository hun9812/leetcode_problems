class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        s_count = 0

        for i in g:
            while s_count < len(s):
                if i <= s[s_count]:
                    s_count += 1
                    res += 1
                    break
                s_count += 1
        
        return res

        