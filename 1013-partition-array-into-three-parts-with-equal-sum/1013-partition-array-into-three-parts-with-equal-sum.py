class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        aim = total // 3
        arr1 = []
        arr2 = []
        check = -1
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
            elif sum(arr1) != aim:
                arr1.append(arr[i])
            elif sum(arr2) != aim:
                arr2.append(arr[i])
            else:
                check = i
                break

        if arr1:
            zero_count += 1
        if arr2:
            zero_count += 1

        if zero_count >= 2 and sum(arr[check:]) == aim:
            return True


        temp = []
        for i in range(check, len(arr)):
            temp.append(arr[i])
            if sum(temp) == aim:
                zero_count += 1

        print(zero_count, check)
        if zero_count >= 3 and sum(arr[check:]) == aim:
            return True
        else:
            return False
        