class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        res = 0
        cur = 0
        been = set()
        
        for i in range(len(nums)):
            while nums[i] in been:
                cur -= nums[left]
                been.remove(nums[left])
                left += 1

            cur += nums[i]
            been.add(nums[i])
            res = max(res, cur)
        
        return res