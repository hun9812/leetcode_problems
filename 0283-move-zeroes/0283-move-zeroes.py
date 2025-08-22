class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                nums[i-count_zero] = nums[i]
        
        for i in range(-1, -(count_zero+1), -1):
            nums[i] = 0

        