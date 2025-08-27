class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        check = False
        for i in nums:
            if i == 1:
                if check:
                    cur += 1
                    res = max(res, cur)
                else:
                    cur = 1
                    res = max(res, 1)
                    check = True
            else:
                cur = 0
                check = False
            
        return res
        