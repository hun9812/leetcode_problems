class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        
        res = max(cur, res)

        return res

        