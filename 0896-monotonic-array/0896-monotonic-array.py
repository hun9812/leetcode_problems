class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = 0
        for i in range(1,len(nums)):
            if nums[n] == nums[i]:
                n += 1
            else:
                break
        if len(nums)-1 == n:
            return True
        
        is_increase = nums[n] < nums[n+1]

        if is_increase:
            for i in range(n+1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
        else:
            for i in range(n+1, len(nums)):
                if nums[i-1] < nums[i]:
                    return False
        return True

        