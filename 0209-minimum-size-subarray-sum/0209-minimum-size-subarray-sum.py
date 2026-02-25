class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        start = 0
        end = 0
        cur_sum = 0
        min_len = 1000000
        
        while end < len(nums):
            cur_sum += nums[end]
            while cur_sum >= target:
                min_len = min(min_len, end-start+1)
                cur_sum -= nums[start]
                start += 1
            end += 1
        
        return min_len
