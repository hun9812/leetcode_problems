class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = 1
        if num < 6:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors += i
                if i != num//i:
                    divisors += num//i
        
        if divisors == num:
            return True
        else:
            return False
        