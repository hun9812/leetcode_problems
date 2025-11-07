class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        clost_dis = 100001
        res = [100001 for _ in range(len(s))]
        
        for i in range(len(s)):
            if s[i] == c:
                clost_dis = 0
            else:
                clost_dis += 1
            res[i] = min(res[i], clost_dis)
        
        clost_dis = 100001
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                clost_dis = 0
            else:
                clost_dis += 1
            res[i] = min(res[i], clost_dis)
        
        return res