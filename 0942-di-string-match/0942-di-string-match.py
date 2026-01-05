class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        max_value = len(s)
        avail_low = 0
        avail_max = max_value
        output = [0 for i in range(len(s)+1)]
        if s[0] == "I":
            output[0] = 0
            avail_low = 1
        else:
            output[0] = avail_max
            avail_max -= 1
        
        
        l = 0
        while l < len(s):
            count = 0
            cur = s[l]
            while l < len(s) and cur == s[l]:
                l += 1
                count += 1
            if cur == "I":
                avail_max -= count
                for i in range(count):
                    output[l-count+i+1] = avail_max + i + 1
                
            else:
                avail_low += count
                for i in range(count):
                    output[l-count+1+i] = avail_low-1-i

        return output

    
        