class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = [[0 for _ in range(len(nums))] for _ in range(4)]

        # res[0]: only odd number
        # res[1]: only even number
        # res[2]: finish with odd number (odd, even, odd, ... , odd)
        # res[3]: finish with even number (odd, even, odd, ... , even)
        if nums[0] % 2 == 1:
            res[0][0] = 1
            res[2][0] = 1
        else:
            res[1][0] = 1
            res[3][0] = 1

        for i in range(1,len(nums)):
            if nums[i] % 2 == 1:
                res[0][i] = res[0][i-1] + 1
                res[1][i] = res[1][i-1]
                res[2][i] = res[3][i-1] + 1
                res[3][i] = res[3][i-1]
            
            else:
                res[0][i] = res[0][i-1]
                res[1][i] = res[1][i-1] + 1
                res[2][i] = res[2][i-1]
                res[3][i] = res[2][i-1] + 1
        
        #print(res)
        k = 0
        for i in range(4):
            if k < res[i][len(nums)-1]:
                k = res[i][len(nums)-1]
        
        return k

