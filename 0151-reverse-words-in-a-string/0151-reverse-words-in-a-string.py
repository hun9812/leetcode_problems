class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = list(s.split())
        s_list = s_list[::-1]
        return " ".join(s_list)