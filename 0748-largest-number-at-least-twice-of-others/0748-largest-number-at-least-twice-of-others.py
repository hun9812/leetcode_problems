class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if nums[0] <= nums[1]:
            first = nums[1]
            second = nums[0]
            index = 1
        else:
            first = nums[0]
            second = nums[1]
            index = 0
        
        for i in range(2, len(nums)):
            if nums[i] > first:
                second = first
                first = nums[i]
                index = i
            elif nums[i] > second:
                second = nums[i]
        
        if second*2 <= first:
            return index
        else:
            return -1
        