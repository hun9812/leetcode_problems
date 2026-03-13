class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        res = 0
        # print(citations)

        for i in range(len(citations)):
            if citations[i] >= i+1:
                #print(citations[i], i)
                res = max(res, i+1)
        
        return res