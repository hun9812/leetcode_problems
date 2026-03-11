class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_index = 0
        entire_product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count == 0:
                    zero_count += 1
                    zero_index = i
                else:
                    zero_count = 2
                    break
            else:
                entire_product *= nums[i]
        
        if zero_count == 2:
            return [0 for _ in range(len(nums))]
        elif zero_count == 1:
            res = [0 for _ in range(len(nums))]
            res[zero_index] = entire_product
            return res
        else:
            res = []
            for num in nums:
                res.append(entire_product // num)
            return res