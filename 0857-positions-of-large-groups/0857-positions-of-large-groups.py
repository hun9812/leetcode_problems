class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        if len(s) < 3:
            return res
        
        cons_count = 1
        start_index = 0
        cur_letter = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cons_count += 1
                if cons_count < 3:
                    continue
                if len(res) >= 1:
                    if res[-1][0] == start_index:
                        res[-1][1] = i
                    else:
                        res.append([start_index, i])
                else:
                    res.append([start_index, i])
            else:
                cons_count = 1
                start_index = i
        
        return res