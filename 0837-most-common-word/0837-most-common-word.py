import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        d = {}
        res = 0
        max_res = ""
        for i in words:
            if i in banned:
                continue
            else:
                if i in d:
                    d[i] += 1
                    if d[i] > res:
                        max_res = i
                        res = d[i]
                else:
                    d[i] = 1
                    if res == 0:
                        max_res = i
                        res = 1
            
        return max_res