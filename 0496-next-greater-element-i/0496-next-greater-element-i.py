class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i in range(len(nums2)):
            dict[nums2[i]] = i
        res = []

        for i in nums1:
            pos = dict[i]
            temp = -1
            for j in range(pos, len(nums2)):
                if nums2[j] > i:
                    temp = nums2[j]
                    break
            res.append(temp)
        
        return res

        