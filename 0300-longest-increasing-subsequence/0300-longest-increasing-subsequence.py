class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        # print(dp)
        return max(dp)