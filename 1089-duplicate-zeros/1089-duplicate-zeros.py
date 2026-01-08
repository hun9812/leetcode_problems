class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        for i in arr:
            if i == 0:
                res.append(i)
                res.append(i)
            else:
                res.append(i)
        arr[:] = res[:len(arr)]