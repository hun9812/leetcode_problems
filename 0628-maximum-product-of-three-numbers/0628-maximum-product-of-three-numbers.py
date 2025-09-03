class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # three positive or 1positive+2negative
        nums.sort()
        res = (-2)**35

        temp = nums[-1] * nums[-2] * nums[-3]
        res = max(res, temp)
        temp = nums[-1] * nums[0] * nums[1]
        res = max(res, temp)

        return res 

        