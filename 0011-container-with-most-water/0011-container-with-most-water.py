class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start = 0
        end = len(height) - 1
        while start < end:
            length = end-start
            cur_h = min(height[start], height[end])
            res = max(res, length * cur_h)
            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                if height[start+1] > height[end-1]:
                    start += 1
                else:
                    end -= 1
        
        return res
        