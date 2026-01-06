class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            temp = {}
            res.append(temp)
            for j in words[i]:
                if j in res[i]:
                    res[i][j] += 1
                else:
                    res[i][j] = 1
        final_res = []
        for i in res[0].keys():
            count = res[0][i]
            for j in range(1, len(res)):
                if i in res[j]:
                    count = min(count, res[j][i])
                else:
                    count = 0
                    break
            if count != 0:
                for k in range(count):
                    final_res.append(i)
        
        return final_res
        