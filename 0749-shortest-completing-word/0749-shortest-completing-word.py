class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l = []
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        for i in licensePlate:
            if i in alphabet:
                i = i.lower()
                l.append(i)
        
        words.sort(key = lambda x: len(x))
        for i in words:
            check = l[:]
            for j in i:
                for k in range(len(check)):
                    if check[k] == j.lower():
                        check[k] = 0
                        break
            for h in range(len(check)):
                if check[h] != 0:
                    break
                if h == len(check)-1:
                    return i
        