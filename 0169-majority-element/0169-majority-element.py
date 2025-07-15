class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        

        res = nums[0]
        
        for i in range(1, len(nums)//2 + 1):
            if dict[nums[i]] > dict[res]:
                res = nums[i]

        return res