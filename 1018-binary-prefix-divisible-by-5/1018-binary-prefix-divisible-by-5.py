class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False for _ in range(len(nums))]
        cur = 0
        for i in range(len(nums)):
            cur = cur<<1
            cur += nums[i]
            if cur % 5 == 0:
                res[i] = True
        
        return res
        