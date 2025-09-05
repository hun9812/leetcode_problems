class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = [1, i, i]
            else:
                dict[nums[i]][0] += 1
                dict[nums[i]][2] = i

        max_freq = [dict[nums[0]]]
        for i in dict.keys():
            if dict[i][0] > max_freq[0][0]:
                max_freq = [dict[i]]
            elif dict[i][0] == max_freq[0][0]:
                max_freq.append(dict[i])

        res = 10**5
        for i in max_freq:
            temp = i[2]-i[1]
            res = min(res, temp)
        
        return res+1
        