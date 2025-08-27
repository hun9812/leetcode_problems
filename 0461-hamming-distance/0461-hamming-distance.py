class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x < y:
            temp = x
            x = y
            y = temp

        x = str(bin(x)[2:])
        y = str(bin(y)[2:])
        extra = x[:len(x)-len(y)]
        extra_count = extra.count('1')
        
        x = x[len(x)-len(y):]
        for i in range(len(y)):
            if x[i] != y[i]:
                extra_count += 1
        
        return extra_count
        