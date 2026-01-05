class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        check = len(nums) // 2
        nums_dict = {}
        for i in range(check+2):
            if nums[i] in nums_dict:
                return nums[i]
            else:
                nums_dict[nums[i]] = True