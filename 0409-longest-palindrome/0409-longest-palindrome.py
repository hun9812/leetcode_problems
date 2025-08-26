class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        s = set(list(s))
        res = 0
        check = False
        for i in s:
            if dict[i] % 2 == 1:
                check = True
            res += (dict[i] // 2 * 2)
        
        if check:
            return res + 1
        else:
            return res