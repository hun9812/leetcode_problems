class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in columnTitle:
            res *= 26
            res += ord(i)-64

        return res 
        