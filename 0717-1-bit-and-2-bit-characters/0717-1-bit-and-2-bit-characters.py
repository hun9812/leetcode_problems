class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        for i in bits[-2::-1]:
            if i == 0:
                break
            else:
                count += 1
        
        if count % 2 == 0:
            return True
        else:
            return False
        