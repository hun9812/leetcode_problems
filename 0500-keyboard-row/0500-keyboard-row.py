class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard1 = 'qwertyuiop'
        keyboard2 = 'asdfghjkl'
        keyboard3 = 'zxcvbnm'
        res = []

        for i in words:
            t = i
            i = i.lower()
            if i[0] in keyboard1:
                temp = True
                for j in i:
                    if j not in keyboard1:
                        temp = False
                if temp:
                    res.append(t)
                
            elif i[0] in keyboard2:
                temp = True
                for j in i:
                    if j not in keyboard2:
                        temp = False
                        break
                if temp:
                    res.append(t)
            elif i[0] in keyboard3:
                temp = True
                for j in i:
                    if j not in keyboard3:
                        temp = False
                        break
                if temp:
                    res.append(t)
        return res            