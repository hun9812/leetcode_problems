class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def make_permute(k):
            # print(k, nums)
            if k == len(nums):
                res.append(nums[:])
                return
            for i in range(k, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                make_permute(k+1)
                nums[i], nums[k] = nums[k], nums[i]
        
        make_permute(0)
        return res
