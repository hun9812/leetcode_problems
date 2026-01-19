class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 1
        check_twice = False
        for i in range(1, len(nums)):
            if not check_twice or nums[i] != nums[cur-1]:
                nums[cur] = nums[i]
                cur += 1
            if nums[cur-1] == nums[cur-2]:
                check_twice = True
            else:
                check_twice = False
        
        return cur

        