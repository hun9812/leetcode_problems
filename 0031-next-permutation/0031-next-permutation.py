class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                check = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1] and nums[check] > nums[j]:
                        check = j
                nums[i-1], nums[check] = nums[check], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
        