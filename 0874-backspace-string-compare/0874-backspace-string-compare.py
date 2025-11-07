class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s = ""
        res_t = ""
        
        backspace_c = 0
        for i in s[::-1]:
            if i == "#":
                backspace_c += 1
            else:
                if backspace_c:
                    backspace_c -= 1
                    continue
                else:
                    res_s += i
        
        backspace_c = 0
        for i in t[::-1]:
            if i == "#":
                backspace_c += 1
            else:
                if backspace_c:
                    backspace_c -= 1
                    continue
                else:
                    res_t += i
        
        if res_t == res_s:
            return True
        else:
            return False