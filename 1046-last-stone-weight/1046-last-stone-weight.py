class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) >= 2:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            res = abs(a-b)
            if res == 0:
                continue
            else:
                stones.append(res)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0