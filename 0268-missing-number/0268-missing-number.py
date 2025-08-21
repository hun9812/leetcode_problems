class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = sum(range(len(nums)+1))
        for i in nums:
            res -= i
        return res

        
        