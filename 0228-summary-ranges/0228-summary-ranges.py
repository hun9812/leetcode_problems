class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out_nums = []
        i = 0
        while i < len(nums):
            start = i
            end = nums[i]
            while (i+1 < len(nums)) and (nums[i+1] == (end + 1)):
                end += 1
                i += 1
            if nums[start] == end:
                out_nums.append("{0}".format(end))
            else:
                out_nums.append("{0}->{1}".format(nums[start],end))
            i+=1

        return out_nums

        