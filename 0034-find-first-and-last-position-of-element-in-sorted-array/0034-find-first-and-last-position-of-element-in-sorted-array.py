class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        start =0
        end = len(nums) - 1
        if len(nums) == 0:
            return [-1,-1]
        if nums[0] == target:
            first = 0
            pass
        else:
            while start <= end:
                cur = (start + end) // 2
                # print(nums[cur], start, end)
                if nums[cur] == target:
                    if cur == 0:
                        first = 0
                        break
                    if nums[cur-1] != target:
                        first = cur
                        break
                    else:
                        first = cur
                        end = cur - 1
                elif nums[cur] < target:
                    start = cur + 1
                else:
                    end = cur - 1

        if first == -1:
            return [-1, -1]

        last = len(nums)-1
        start = first
        end = last
        if nums[last] == target:
            pass
        else:
            while start <= end:
                cur = (start + end) // 2
                if nums[cur] == target:
                    if cur == len(nums)-1:
                        last = 0
                        break
                    if nums[cur+1] != target:
                        last = cur
                        break
                    else:
                        last = cur
                        start = cur + 1
                elif nums[cur] < target:
                    start = cur+ 1
                else:
                    end = cur - 1

        return [first, last]