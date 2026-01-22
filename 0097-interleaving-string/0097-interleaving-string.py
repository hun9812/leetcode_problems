from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def make_it(cur1, cur2):
            cur3 = cur1+cur2
            if cur1 == len(s1) and cur2 == len(s2):
                return True
            res = False
            if cur1 < len(s1) and s1[cur1] == s3[cur3]:
                res = res or make_it(cur1+1, cur2)
            if cur2 < len(s2) and s2[cur2] == s3[cur3]:
                res = res or make_it(cur1, cur2+1)
            
            return res
        
        return make_it(0,0)