class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # pigeonhole principle
        if len(nums) == 1:
            return 0
        min_num = nums[0]
        max_num = nums[0]
        for i in range(1, len(nums)):
            min_num = min(min_num, nums[i])
            max_num = max(max_num, nums[i])

        if min_num == max_num:
            return 0
        size = max(1, (max_num - min_num) // (len(nums)-1))
        bucket = [[None, None] for _ in range((max_num - min_num) // size + 1)]

        for num in nums:
            idx = (num - min_num) // size
            if bucket[idx][0] is None:
                bucket[idx][0] = num
                bucket[idx][1] = num
            else:
                bucket[idx][0] = min(bucket[idx][0], num)
                bucket[idx][1] = max(bucket[idx][1], num)
        
        max_size = 0
        prev_max = min_num

        for b in bucket:
            if b[0] is not None:
                max_size = max(max_size, b[0] - prev_max)
                prev_max = b[1]
        
        return max_size
        
        
        
        # if len(nums) == 1:
        #     return 0
        
        # nums.sort()
        # res = nums[1]-nums[0]
        # for i in range(2, len(nums)):
        #     res = max(res, nums[i]-nums[i-1])
        
        # return res