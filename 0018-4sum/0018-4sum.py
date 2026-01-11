class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for a in range(len(nums)-3):
            for d in range(a+3, len(nums)):
                b = a+1
                c = d-1
                two_target = target - nums[a] - nums[d]
                while (b < c):
                    # print(a, b, c, d)
                    cur = nums[b] + nums[c]
                    if cur == two_target:
                        res.add((nums[a], nums[b], nums[c], nums[d]))
                        b += 1
                        c -= 1
                    elif cur > two_target:
                        c -= 1
                    else:
                        b += 1
            
    
        
        return list(res)
        