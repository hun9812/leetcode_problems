class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            left = False
            right = False
            try:
                if flowerbed[i-1] == 0:
                    left = True
            except:
                left = True
            if i == 0:
                left = True

            try:
                if flowerbed[i+1] == 0:
                    right = True
            except:
                right = True

            if left and right:
                n -= 1
                flowerbed[i] = 1
                
                
        if n <= 0:
            return True
        else:
            return False
        