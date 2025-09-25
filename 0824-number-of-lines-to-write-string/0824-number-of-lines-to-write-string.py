class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        output = [1, 0]
        
        for i in s:
            length = widths[abs(ord(i)-ord("a"))]
            if output[1] + length > 100:
                output[0] += 1
                output[1] = length
            else:
                output[1] += length
        
        return output
        