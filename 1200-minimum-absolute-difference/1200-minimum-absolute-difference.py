class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_diff = 2 ** 30
        arr.sort()
        for i in range(1, len(arr)):
            min_diff = min(arr[i]-arr[i-1], min_diff)
        
        res = []
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == min_diff:
                res.append([arr[i-1], arr[i]])
        
        return res

        