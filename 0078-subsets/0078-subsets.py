class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = nums[::-1]

        def make_subset(cur, rem):
            # print(res)
            if not rem:
                return
            a = rem.pop()
            cur.append(a)
            res.append(cur[:])
            make_subset(cur, rem[:])
            cur.pop()
            make_subset(cur, rem[:])
            
        
        make_subset([], nums)
        res.append([])
        return res