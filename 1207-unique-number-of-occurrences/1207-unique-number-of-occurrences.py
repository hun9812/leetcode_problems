class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        num_dict = {}
        occurs = [0 for i in range(1001)]

        for i in arr:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1

            occurs[num_dict[i]] += 1
            occurs[num_dict[i]-1] -= 1
        
        for i in range(1, 1001):
            if occurs[i] >= 2:
                return False

        return True