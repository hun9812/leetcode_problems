class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        remain = [0,0,0]
        
        for bill in bills:
            if bill == 5:
                remain[0] += 1
            elif bill == 10:
                remain[1] += 1
                remain[0] -= 1
                if remain[0] < 0:
                    return False
            else:
                remain[2] += 1
                if remain[1]:
                    remain[1] -= 1
                    remain[0] -= 1
                    if remain[0] < 0:
                        return False
                else:
                    remain[0] -= 3
                    if remain[0] < 0:
                        return False
        return True
        