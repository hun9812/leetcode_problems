class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        first = s[0]
        if len(s) == 1:
            return False
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False

        for i in range(1, len(s)//2+1):
            if s[i] == first:
                if len(s) % i != 0:
                    continue
                # 0 ~ i-1 까지가 패턴: (i) 개 숫자
                for j in range(i, len(s)):
                    if s[j] == s[j%i]:
                        if j == len(s)-1:
                            return True
                        continue
                    else:
                        break
        return False


        