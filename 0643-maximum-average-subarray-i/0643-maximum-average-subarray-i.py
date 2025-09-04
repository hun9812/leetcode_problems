class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        cur = max_sum
        for i in range(k, len(nums)):
            cur = cur + nums[i] - nums[i-k]
            max_sum = max(cur, max_sum)

        return max_sum/k
        