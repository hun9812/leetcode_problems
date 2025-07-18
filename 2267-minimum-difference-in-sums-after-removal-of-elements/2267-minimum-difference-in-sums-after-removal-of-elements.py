import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        k = len(nums) // 3
        nums1 = nums[:k]
        nums2 = nums[k:]
        nums1.sort()
        nums2.sort()
        sum_nums1 = sum(nums1)
        sum_nums2 = sum(nums2[k:])

        res = sum_nums1 - sum_nums2

        for i in range(k, 2*k):
            temp = nums[i]

            if temp < nums1[k-1]:
                sum_nums1 = sum_nums1 + temp - nums1[k-1]
            bisect.insort(nums1, temp)
            # nums1 done, sorted, i elements
            
            idx = bisect.bisect_left(nums2, temp)
            if idx > len(nums2)-k-1:
                sum_nums2 = sum_nums2 - temp + nums2[-k-1]

            del nums2[idx]
            # nums2 done, sorted, 3k-i element
            res = min(res, sum_nums1 - sum_nums2)
        
        return res





