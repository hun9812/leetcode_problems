class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        complement = ""
        for i in n:
            if i == "0":
                complement += "1"
            else:
                complement += "0"
        count = 0
        for j in complement:
            if j == "0":
                count += 1
            else:
                break
        complement = complement[count:]
        if complement == "":
            complement = "0"
        res = int(complement, 2)
        return res