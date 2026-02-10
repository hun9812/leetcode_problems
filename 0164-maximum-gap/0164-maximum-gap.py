class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        res = nums[1]-nums[0]
        for i in range(2, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        
        return res