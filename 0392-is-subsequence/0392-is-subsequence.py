class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_check = 0
        t_check = 0
        while s_check < len(s) and t_check < len(t):
            if s[s_check] == t[t_check]:
                s_check += 1
                t_check += 1
            else:
                t_check += 1

        if s_check == len(s):
            return True
        else:
            return False 
        