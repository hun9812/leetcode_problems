class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # just find 2 nums, then can decide remain things
        
        def is_valid(num1, num2, k):
            if num1[0] == "0" and len(num1) > 1:
                return False
            if num2[0] == "0" and len(num2) > 1:
                return False
            cur = str(int(num1) + int(num2))
            if k + len(cur) > len(num):
                return False
            if num[k:k+len(cur)] == cur:
                if k + len(cur) == len(num):
                    return True
                else:
                    return is_valid(num2, cur, k+len(cur))
        
        for i in range(1, len(num)-1):
            for j in range(1, (len(num)-i) // 2 + 1):
                if is_valid(num[:i], num[i:i+j], i+j):
                    # print(i,j)
                    return True
        
        return False

