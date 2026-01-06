class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        changed = 0
        for i in range(k):
            if len(nums) <= i:
                break
            if nums[i] >= 0:
                break
            else:
                changed += 1
                nums[i] = -nums[i]
        if changed == k:
            return sum(nums)
        nums.sort()
        if (k-changed) % 2 == 1 and k > changed:
            nums[0] = -nums[0]
        return sum(nums)
        