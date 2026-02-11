class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        for i in range(len(s)-10):
            if s[i:i+10] in s[i+1:]:
                res.add(s[i:i+10])
        
        return list(res)