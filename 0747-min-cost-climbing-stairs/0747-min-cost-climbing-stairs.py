class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0 for _ in range(len(cost))]
        res[0] = cost[0]
        res[1] = cost[1]

        for i in range(2, len(cost)):
            res[i] = min(res[i-1], res[i-2]) + cost[i]
            
        
        return min(res[-1], res[-2])
        