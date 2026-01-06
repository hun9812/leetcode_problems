class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ""
        for i in num:
            num_str += str(i)
        k = str(k)
        k = k[::-1]
        num_str = num_str[::-1]
        
        same_len = max(len(num_str), len(k))
        if same_len == len(num_str):
            for _ in range(same_len - len(k)):
                k += "0"
        else:
            for _ in range(same_len - len(num_str)):
                num_str += "0"
        
        remain = 0
        res = []
        for i in range(same_len):
            cur = int(num_str[i]) + int(k[i]) + remain
            cur = str(cur)
            if len(cur) == 1:
                remain = 0
                res.append(int(cur))
            else:
                remain = 1
                res.append(int(cur[-1]))
        
        if remain == 1:
            res.append(1)
        
        return res[::-1]

        