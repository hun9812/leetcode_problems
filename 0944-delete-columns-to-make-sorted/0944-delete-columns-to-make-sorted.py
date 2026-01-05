class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for column in range(len(strs[0])):
            for row in range(1,len(strs)):
                if ord(strs[row][column]) < ord(strs[row-1][column]):
                    res += 1
                    break
        return res