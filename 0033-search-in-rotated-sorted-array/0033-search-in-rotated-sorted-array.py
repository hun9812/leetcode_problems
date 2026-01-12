class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a =self.search_index(nums, 0, len(nums)-1)
        if a == -1:
            return self.binary_search(nums,target, 0, len(nums)-1)
        else:
            return max(self.binary_search(nums, target, 0, a),
                       self.binary_search(nums,target, a+1,len(nums)-1))

    def search_index(self, nums, start, end):
        if start >= end:
            return -1
        temp = (start + end) // 2
        if nums[temp] > nums[temp+1]:
            return temp
        else:
            return max(self.search_index(nums, start, temp), self.search_index(nums, temp+1, end))

    def binary_search(self, nums, target, start, end):
        print(start, end)
        if start > end:
            return -1
        elif start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        else:
            temp = (start + end) // 2
            if nums[temp] == target:
                return temp
            elif nums[temp] < target:
                return self.binary_search(nums, target, temp+1, end)
            else:
                return self.binary_search(nums, target, start, temp-1)