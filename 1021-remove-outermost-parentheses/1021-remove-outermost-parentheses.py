class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        comp = [0,1, 1]
        for i in range(1, len(s)):
            if s[i] == "(":
                comp[1] += 1
                comp[2] += 1
            else:
                comp[1] -= 1
                comp[2] += 1
                if comp[1] == 0:
                    res += s[comp[0]+1 : comp[0] + comp[2]-1]
                    comp = [i+1, 0,0]
        return res
        