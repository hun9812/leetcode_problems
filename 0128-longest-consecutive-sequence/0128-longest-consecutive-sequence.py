class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev = -2**31
        cur_len = 0
        res = 0

        for i in nums:
            if prev == i:
                continue
            elif prev+1 == i:
                cur_len += 1
                res = max(res, cur_len)
                prev = i
            else:
                prev = i
                cur_len = 1
        
        return max(res, cur_len)