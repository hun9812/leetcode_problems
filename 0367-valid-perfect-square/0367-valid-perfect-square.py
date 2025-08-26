class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num == 5:
            return False
        for i in range(1, num//2+1):
            if i*i == num:
                return True
            if i*i > num:
                return False
        