class Solution:
    def grayCode(self, n: int) -> List[int]:
        num = 2 ** n
        res = []

        for i in range(num):
            res.append(i^(i>>1))

        return res