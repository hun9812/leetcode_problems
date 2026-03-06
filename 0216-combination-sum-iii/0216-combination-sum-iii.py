class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []

        def find_sum(num, k, n, cur):
            if k == 0 and n == 0:
                self.res.append(cur[:])
                return
            if k <= 0 or n <= 0 or num > 9:
                return

            for i in range(num, 10):
                if n - i < 0:
                    break
                cur.append(i)
                find_sum(i+1, k-1, n-i, cur)
                cur.pop()
                
        find_sum(1, k, n, [])
        return self.res
