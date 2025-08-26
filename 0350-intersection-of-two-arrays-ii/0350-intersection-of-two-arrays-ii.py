class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        itsc = nums1_set.intersection(nums2_set)
        itsc = list(itsc)

   

        for i in range(len(itsc)):
            p = itsc[i]
            n1 = nums1.count(p)-1
            n2 = nums2.count(p)-1

            for j in range(min(n1,n2)):
                itsc.append(p)
        
        return itsc

        