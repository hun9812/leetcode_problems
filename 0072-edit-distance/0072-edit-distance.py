class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        res = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

        for i in range(len(word1)+1):
            res[0][i] = i
        for i in range(len(word2)+1):
            res[i][0] = i

        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1]) + 1 
        
        return res[len(word2)][len(word1)]










        # #output = max(len(word1), len(word2))

        # def divcon(w1, w2):
        #     if len(w1) == 0:
        #         return len(w2)
        #     if len(w2) == 0:
        #         return len(w1)
            
        #     res = max(len(w1), len(w2))
        #     for i in range(len(w1)):
        #         idx = w2.find(w1[i])
        #         if idx == -1:
        #             continue
        #         elif abs(i-idx) + abs((len(w1)-i) - (len(w2)-idx)) > res:
        #             # print(res, w1, w2, i, idx, abs(i-idx) + abs((len(w1)-i) - (len(w2)-idx)))
        #             continue
        #         else:
        #             if i == len(w1)-1:
        #                 cur = divcon(w1[:i], w2[:idx]) + len(w2) - (idx+1)
        #             elif idx == len(w2)-1:
        #                 cur = divcon(w1[:i], w2[:idx]) + len(w1) - (i+1)
        #             else:
        #                 cur = divcon(w1[:i], w2[:idx]) + divcon(w1[i+1:], w2[idx+1:])
        #             res = min(res, cur)
        #     return res
        
        # output = divcon(word1, word2)

        # return output