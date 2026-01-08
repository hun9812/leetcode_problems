class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_in_arr2 = []
        arr1_count = {}

        for i in arr1:
            if i in arr2:
                if i in arr1_count:
                    arr1_count[i] += 1
                else:
                    arr1_count[i] = 1
            else:
                not_in_arr2.append(i)
        res = []
        for i in arr2:
            for j in range(arr1_count[i]):
                res.append(i)
        
        not_in_arr2.sort()
        for i in not_in_arr2:
            res.append(i)
        
        return res