# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1; end = n
        while (start<=end):
            pivot = (start + end) // 2
            ans = guess(pivot)
            if ans == -1:
                end = pivot-1
            elif ans == 1:
                start = pivot + 1
            else:
                return pivot
        