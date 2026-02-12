class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2,5
        res = [0,0]
        for i in range(2,n+1):
            temp = i
            while temp%2 ==0:
                res[0] += 1
                temp = temp // 2
            while temp%5 == 0:
                res[1] += 1
                temp = temp // 5
        
        return min(res)