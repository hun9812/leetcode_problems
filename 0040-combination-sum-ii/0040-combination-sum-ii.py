class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def backtrack(remain, curr_list, start):
            if remain == 0:
                res.append(list(curr_list))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if remain - candidates[i] < 0:
                    break
                
                curr_list.append(candidates[i])
                backtrack(remain - candidates[i], curr_list, i + 1)
                curr_list.pop()

        backtrack(target, [], 0)
        return list(res)