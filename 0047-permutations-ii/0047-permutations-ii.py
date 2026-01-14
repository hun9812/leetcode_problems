class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        been = [False for _ in range(len(nums))]
        cur = []

        def make_unique_permute():
            print(cur)
            if len(nums) == len(cur):
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                if been[i] is True:
                    continue
                
                if (i > 0) and (nums[i] == nums[i-1]) and (been[i-1] is False):
                    continue
                else:
                    been[i] = True
                    cur.append(nums[i])
                    make_unique_permute()
                    cur.pop()
                    been[i] = False
        
        make_unique_permute()
        return res