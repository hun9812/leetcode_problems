class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        be_trusted = [0 for i in range(n+1)]
        trust_someone = [False for i in range(n+1)]
        for i in trust:
            trust_someone[i[0]] = True
            be_trusted[i[1]] += 1
        
        for i in range(1, n+1):
            if be_trusted[i] == n-1:
                if trust_someone[i] is False:
                    return i
        return -1

        