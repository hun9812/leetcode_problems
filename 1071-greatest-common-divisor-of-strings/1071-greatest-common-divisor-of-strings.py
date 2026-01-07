class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        for i in range(1,len(str2)+1):
            pos = str2[:i]
            if len(str1) % len(pos) == 0 and len(str2) % len(pos) == 0:
                check = True
                for j in range(len(str1)//len(pos)):
                    if not check:
                        break
                    for k in range(i):
                        if str1[i*j + k] != pos[k]:
                            check = False
                            break
                for j in range(len(str2)//len(pos)):
                    if not check:
                        break
                    for k in range(i):
                        if str2[i*j + k] != pos[k]:
                            check = False
                            break 
                if check:
                    res = pos
        return res
        