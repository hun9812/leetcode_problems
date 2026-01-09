class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                temp = (nums[i], nums[j], nums[k])
                if sum(temp) == 0:
                    res.add(temp)
                    j += 1
                    k -= 1
                elif sum(temp) > 0:
                    k -= 1
                else:
                    j += 1
        return list(res)