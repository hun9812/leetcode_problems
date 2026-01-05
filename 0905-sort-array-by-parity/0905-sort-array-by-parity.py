class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_even_plus_one = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[last_even_plus_one] = nums[last_even_plus_one], nums[i]
                last_even_plus_one += 1
        return nums