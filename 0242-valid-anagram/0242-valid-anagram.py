class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for i in t:
            if i in dict:
                if dict[i] == 0:
                    return False
                else:
                    dict[i] -= 1
            else:
                return False
        
        for i in s:
            if dict[i] != 0:
                return False

        return True
        