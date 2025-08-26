class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        F = "Fizz"
        B = "Buzz"
        FB = "FizzBuzz"
        res = []

        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    res.append(FB)
                    continue
                res.append(F)
                continue
            if i % 5 == 0:
                res.append(B)
                continue
            res.append(str(i))
        
        return res
        