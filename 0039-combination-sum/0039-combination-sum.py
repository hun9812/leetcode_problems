class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, curr_list, start):
            if remain == 0:
                res.append(list(curr_list))
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                curr_list.append(candidates[i])
                backtrack(remain - candidates[i], curr_list, i)
                curr_list.pop()

        backtrack(target, [], 0)
        return res