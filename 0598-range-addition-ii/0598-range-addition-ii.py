class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n

        for i in ops:
            if i[0] <= min_m and i[1] <= min_n:
                min_m = i[0]
                min_n = i[1]
            else:
                # 둘이 겹치는 작은 부위로
                min_m = min(min_m, i[0])
                min_n = min(min_n, i[1])

        return min_m * min_n