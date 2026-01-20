class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binary_search(start, end):
            if start > end:
                return False
            
            mid = (start + end) // 2
            if nums[mid] == target:
                return True

            if nums[start] == nums[mid] and nums[mid] == nums[end]:
                return binary_search(start + 1, end - 1)
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return binary_search(start, mid - 1)
                else:
                    return binary_search(mid + 1, end)
            else:
                if nums[mid] < target <= nums[end]:
                    return binary_search(mid + 1, end)
                else:
                    return binary_search(start, mid - 1)

        return binary_search(0, len(nums) - 1)