class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        res = ""
        for i in range(len(s_list)):
            res += s_list[i][::-1]
            if i != len(s_list)-1:
                res += " "
        
        return res