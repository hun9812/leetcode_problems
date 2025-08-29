class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dict = {}
        for i in candyType:
            if i in dict:
                continue
            else:
                dict[i] = True
        
        return min(len(candyType)//2, len(dict))
        