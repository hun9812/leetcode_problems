class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        
        for i in t:
            if i in s_dict:
                if s_dict[i] == t_dict[i]:
                    continue
                else:
                    return i
            else:
                return i
        