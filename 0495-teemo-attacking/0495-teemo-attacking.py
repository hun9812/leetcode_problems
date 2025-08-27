class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.append(10**8)
        attacked = 0
        res = 0
        for i in range(1, len(timeSeries)):
            term = timeSeries[i] - timeSeries[i-1]
            if duration < term:
                res += attacked
                attacked = 0
                res += duration
            else:
                attacked += term
        
        return res
        