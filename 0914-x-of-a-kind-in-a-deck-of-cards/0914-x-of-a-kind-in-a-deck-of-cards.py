class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        nums_dict = {}
        for i in deck:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        value_list = list(nums_dict.values())
        min_value = min(value_list)
        check = True
        for i in range(2, min_value+1):
            check = True
            for j in value_list:
                if j % i != 0:
                    check = False
            if check is True:
                return True
        
        return False

        