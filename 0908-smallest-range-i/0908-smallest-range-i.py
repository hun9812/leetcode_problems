class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums_min = min(nums)
        nums_max = max(nums)
        diff = nums_max - nums_min
        
        if diff % 2 == 0:
            diff //= 2
            check = (diff - k) * 2
            return max(check, 0)
        else:
            diff //= 2
            check = (diff - k) * 2
            if check == 0:
                return 1
            else:
                return max(check+1, 0)

        