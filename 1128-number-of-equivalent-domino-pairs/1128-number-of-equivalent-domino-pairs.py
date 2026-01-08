class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        paired = [False for _ in range(len(dominoes))]
        res = 0
        for i in range(len(dominoes)):
            if paired[i] == True:
                continue
            cur = 0
            for j in range(i+1, len(dominoes)):
                if paired[j] == False and dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]:
                    paired[j] = True
                    cur += 1
                    # print(i, j)
                elif paired[j] == False and dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0]:
                    paired[j] = True
                    cur += 1
                    # print(i, j)
            if cur != 0:
                for k in range(1, cur+1):
                    res += k
        return res