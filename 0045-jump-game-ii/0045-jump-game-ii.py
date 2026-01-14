class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = [0 for _ in range(len(nums))]
        res[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            cur = 2**31 - 2
            for j in range(1, nums[i]+1):
                if i+j > len(nums)-1:
                    break
                cur = min(cur, res[i+j])
            res[i] = cur+1
        # print(res)
        return res[0]
        