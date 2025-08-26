class Solution:
    def arrangeCoins(self, n: int) -> int:
        temp = n
        for i in range(1,n+1):
            temp -= i
            if temp < 0:
                return i-1
            if temp == 0:
                return i
        