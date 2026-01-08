class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_list = [0 for _ in range(26)]
        for i in chars:
            chars_list[ord(i)-ord("a")] += 1
        
        res = 0
        temp = []
        for i in words:
            temp[:] = chars_list[:]
            check = True
            for j in i:
                temp[ord(j)-ord("a")] -= 1
                if temp[ord(j)-ord("a")] < 0:
                    check = False
                    break
            if check:
                res += len(i)
        return res