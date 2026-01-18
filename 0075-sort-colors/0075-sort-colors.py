class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_dict = {0:0, 1:0, 2:0}
        for i in nums:
            num_dict[i] += 1
        
        for i in range(len(nums)):
            if num_dict[0] > 0:
                nums[i] = 0
                num_dict[0] -= 1
            elif num_dict[1] > 0:
                nums[i] = 1
                num_dict[1] -= 1
            else:
                nums[i] = 2
        