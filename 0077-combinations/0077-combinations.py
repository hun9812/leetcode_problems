class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur = 1
        res = []

        def make_combi(cur, num, k):
            if k == 0:
                res.append(cur[:])
                return
            if num > n:
                return
            cur.append(num)
            make_combi(cur, num+1, k-1)
            cur.pop()
            make_combi(cur, num+1, k)
        make_combi([], 1, k)
        return res