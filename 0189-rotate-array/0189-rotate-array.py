class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse_list(list, start, end):
            while start < end:
                list[start], list[end] = list[end], list[start]
                start += 1
                end -= 1
        
        reverse_list(nums, 0, n-1)
        reverse_list(nums, 0, k-1)
        reverse_list(nums, k, n-1)