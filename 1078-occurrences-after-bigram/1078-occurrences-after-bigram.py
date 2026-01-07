class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = list(text.split(" "))
        res = []
        for i in range(len(text)-2):
            if text[i] == first:
                if text[i+1] == second:
                    res.append(text[i+2])
        return res