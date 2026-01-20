class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False for _ in range(len(nums))]
        res = []

        def subset(cur, cur_res):
            #print(cur, cur_res)
            if cur == len(nums):
                res.append(cur_res[:])
                return
            if cur >= 1 and nums[cur] == nums[cur-1] and visited[cur-1] == False:
                subset(cur+1, cur_res)
            else:
                cur_res.append(nums[cur])
                visited[cur] = True
                subset(cur+1, cur_res)
                cur_res.pop()
                visited[cur] = False
                subset(cur+1, cur_res)
        subset(0,[])

        return res
