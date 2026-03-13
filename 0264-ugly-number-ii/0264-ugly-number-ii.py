class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2 = i3 = i5 = 0
        ugly = [1]

        for i in range(1, n):
            next_i2 = ugly[i2] * 2
            next_i3 = ugly[i3] * 3
            next_i5 = ugly[i5] * 5
            cur_ugly = min(next_i2, next_i3, next_i5)

            ugly.append(cur_ugly)
            if cur_ugly == next_i2:
                i2 += 1
            if cur_ugly == next_i3:
                i3 += 1
            if cur_ugly == next_i5:
                i5 += 1
        
        return ugly[-1]