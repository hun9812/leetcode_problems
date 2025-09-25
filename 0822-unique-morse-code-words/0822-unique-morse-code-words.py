class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {}
        for i in words:
            change = ""
            for j in i:
                change += table[abs(ord("a")-ord(j))]
            if change not in d:
                d[change] = True
        
        return len(d)