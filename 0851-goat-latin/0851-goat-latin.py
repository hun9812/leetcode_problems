class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a_count = 1
        res = ""
        sentence_list = list(sentence.split(" "))
        aeiou = "aeiouAEIOU"

        for s in sentence_list:
            temp = ""
            if s[0] not in aeiou:
                temp = s[1:] + s[0] + "ma" + ("a"*a_count)
            else:
                temp = s + "ma" + ("a"*a_count)
            temp += " "
            res += temp
            a_count += 1
            
        res = res[:-1]
        return res
        