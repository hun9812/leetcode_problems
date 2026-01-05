class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            min_len = min(len(prev), len(cur))
            for j in range(min_len):
                prev_c = order.find(prev[j])
                cur_c = order.find(cur[j])
                if prev_c < cur_c:
                    break
                elif prev_c > cur_c:
                    return False
                if j == min_len-1:
                    if len(prev) == len(cur):
                        continue
                    elif len(prev) > len(cur):
                        return False
                    else:
                        continue

        return True
        