class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        s = ""
        self.makepairs(s, n, n)
        return self.res

    
    def makepairs(self, cur, start_left, end_left):
        if start_left < 0 or end_left < 0:
            return
        if start_left == 0 and end_left == 1:
            cur += ")"
            self.res.append(cur)
            return
        if start_left > end_left:
            return
        elif start_left == end_left:
            cur += "("
            self.makepairs(cur, start_left - 1, end_left)
        else:
            temp = cur
            temp += "("
            self.makepairs(temp, start_left -1, end_left)
            temp2 = cur
            temp2 += ")"
            self.makepairs(temp2, start_left, end_left-1)
        