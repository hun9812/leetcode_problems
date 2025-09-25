class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # for i in range(len(goal)):
        #     if goal[i:] == s[:len(goal)-i]:
        #         if s[-i:] == goal[:i]:
        #             return True
        
        # return False
        if len(s) != len(goal):
            return False

        s = s*2
        if goal in s:
            return True
        else:
            return False

        