class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        cur_min = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            
            temp = cur_max * nums[i]
            cur_max = max(temp, cur_min * nums[i], nums[i])
            cur_min = min(temp, cur_min * nums[i], nums[i])
            
            
            res = max(res, cur_max)
            #print(nums[i], cur_min, cur_max, temp, res)
        
        return res