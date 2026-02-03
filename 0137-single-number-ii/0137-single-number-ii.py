class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict = {}

        for i in nums:
            if i not in num_dict:
                num_dict[i] = False
                continue
            if num_dict[i] == False:
                num_dict[i] = True
                continue
            del num_dict[i]
        
        return list(num_dict.keys())[0]