class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        next_even = 0
        next_odd = 1
        res_list = [0 for i in range(len(nums))]
        
        for i in nums:
            if i % 2 == 0:
                res_list[next_even] = i
                next_even += 2
            else:
                res_list[next_odd] = i
                next_odd += 2
        
        return res_list
        