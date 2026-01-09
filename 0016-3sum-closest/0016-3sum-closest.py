class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 2**31-1
        res_value = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                temp = (nums[i], nums[j], nums[k])
                #print(i,j,k,sum(temp))
                if sum(temp) == target:
                    return target
                    j += 1
                    k -= 1
                elif sum(temp) > target:
                    k -= 1
                    if res > abs(sum(temp)-target):
                        res_value = sum(temp)
                        res = abs(sum(temp) - target)
                    
                else:
                    j += 1
                    if res > abs(sum(temp)-target):
                        res_value = sum(temp)
                        res = abs(sum(temp) - target)
        #print(res_value)
        return res_value