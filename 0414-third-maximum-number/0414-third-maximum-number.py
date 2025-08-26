class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return(max(nums))
        
        # 3 * O(n)
        check = max(nums)
        for _ in range(2):
            p = max(nums)
            for i in range(len(nums)):
                if nums[i] == p:
                    nums[i] = (-2 ** 31) - 1
        
        res = max(nums)
        if res == (-2 ** 31) - 1:
            return check
        else:
            return res

        