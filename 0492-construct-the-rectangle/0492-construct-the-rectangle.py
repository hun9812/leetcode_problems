class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = [area, 1]

        for i in range(2, area//2 + 1):
            if area % i == 0:
                check = area // i
                if check < i:
                    break
                res = [check, i]
        
        return res
        