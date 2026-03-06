class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        res = nums[0]
        
        rob_check = [[0,0] for _ in range(len(nums))]

        rob_check[0][1] = nums[0]
        
        for i in range(1, len(nums)-1):
            rob_check[i][0] = max(rob_check[i-1])
            rob_check[i][1] = rob_check[i-1][0] + nums[i]
        res = max(res, rob_check[len(nums)-2][0], rob_check[len(nums)-2][1])

        rob_check = [[0,0] for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            rob_check[i][0] = max(rob_check[i-1])
            rob_check[i][1] = rob_check[i-1][0] + nums[i]
        
        res = max(res, rob_check[len(nums)-1][0], rob_check[len(nums)-1][1])

        return res

