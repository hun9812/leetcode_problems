class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        res = 0
        prev = 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cur += 1
            else:
                if prev != 0:
                    res = max(res, prev+cur)
                if nums[i] - nums[i-1] == 1:
                    prev = cur
                    cur = 1
                else:
                    prev = 0
                    cur = 1
        
        if prev != 0:
            res = max(res, prev+cur)
        return res