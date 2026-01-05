class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        desc = False
        for i in range(1,len(arr)):
            if desc:
                if arr[i-1] <= arr[i]:
                    return False
            else:
                if arr[i-1] < arr[i]:
                    continue
                elif arr[i-1] == arr[i]:
                    return False
                else:
                    desc = True
        if not desc:
            return False
        else:
            return True
        