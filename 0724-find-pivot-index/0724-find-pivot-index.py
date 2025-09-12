class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        first_sum = 0
        last_sum = sum(nums[1:])
        if first_sum == last_sum:
            return 0
        
        for i in range(1,len(nums)):
            first_sum += nums[i-1]
            last_sum -= nums[i]
            if first_sum == last_sum:
                return i
            # print(i, first_sum, last_sum)
        
        return -1
        