class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        check = 100000
        res = 0
        for i in prices:
            if i <= check:
                check = i
            else:
                res += (i - check)
                check = i
        
        return res
        