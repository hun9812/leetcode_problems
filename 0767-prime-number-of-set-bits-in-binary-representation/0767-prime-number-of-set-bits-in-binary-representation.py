class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            str_i = bin(i)[2:]
            count_1 = str_i.count('1')
            for j in range(2, count_1+1):
                if count_1 % j == 0:
                    if count_1 == j:
                        res += 1
                    else:
                        break
        
        return res
        