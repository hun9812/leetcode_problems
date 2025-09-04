class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict = {}
        double = 0

        for i in nums:
            if i in dict:
                double = i
                break
            else:
                dict[i] = True
        
        original_sum = sum(range(1, len(nums)+1))
        cur_sum = sum(nums) - double

        res = [double, original_sum-cur_sum]
        return res