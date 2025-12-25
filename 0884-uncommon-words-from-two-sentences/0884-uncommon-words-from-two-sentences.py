class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_c = set()
        removed = set()
        for i in list(s1.split(" ")):
            if i in removed:
                continue
            if i in s1_c:
                s1_c.remove(i)
                removed.add(i)
                continue
            s1_c.add(i)

        for i in list(s2.split(" ")):
            if i in removed:
                continue
            if i in s1_c:
                s1_c.remove(i)
                removed.add(i)
                continue
            s1_c.add(i)
        
        res = []
        for i in s1_c:
            res.append(i)

        return res
        