class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        res = [[1 for _ in range(len(nums))] for _ in range(k)]
        c = 0

        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                remain = (nums[i] + nums[j]) % k
                res[remain][i] = max(res[remain][i], res[remain][j] + 1)
                c = max(c, res[remain][i])
        
        return c
            
        