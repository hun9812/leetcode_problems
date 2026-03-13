class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_xor = 0
        for i in nums:
            num_xor = num_xor ^ i
        
        # print(str(bin(num_xor)))
        num_xor = num_xor & (-num_xor)
        # print(str(bin(num_xor)))

        a = 0
        b = 0
        for i in nums:
            if num_xor & i != 0:
                a = a ^ i
            else:
                b = b^ i
        
        return [a,b]