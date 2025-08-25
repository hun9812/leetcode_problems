class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        check = 'aeiouAEIOU'
        start = 0; end = len(s) -1
        while (start < end):
            if s[start] in check:
                if s[end] in check:
                    temp = s[start]
                    s[start] = s[end]
                    s[end] = temp
                    start += 1
                    end -= 1
                    continue
                end -= 1
                continue
            else:
                start += 1
        return ''.join(s)