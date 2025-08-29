class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {}
        for i in range(len(list1)):
            dict[list1[i]] = i

        res = []
        cur = 10000000

        for i in range(len(list2)):
            if list2[i] in dict:
                if dict[list2[i]] + i < cur:
                    res = []
                    res.append(list2[i])
                    cur = dict[list2[i]] + i
                elif dict[list2[i]] + i == cur:
                    res.append(list2[i]) 

        return res