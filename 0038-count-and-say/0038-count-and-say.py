class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1"]
        for i in range(n-1):
            prev = res[-1]
            cur = ""
            check = prev[0]
            count = 0
            for c in prev:
                if c == check:
                    count += 1
                else:
                    cur += str(count)
                    cur += check
                    count = 1
                    check = c
            cur += str(count)
            cur += check
            res.append(cur)
        
        return res[n-1]

        