class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                a = self.isPalindrome(s[i+1:len(s)-i])
                b = self.isPalindrome(s[i:len(s)-(i+1)])
                if a or b:
                    return True
                else:
                    return False
        return True

    
    def isPalindrome(self, st):
        for i in range(len(st)//2):
            if st[i] != st[-(i+1)]:
                return False
        
        return True
        