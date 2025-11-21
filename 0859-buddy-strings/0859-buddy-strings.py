class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        alpha_count = [0 for i in range(26)]
        diff_count = 0
        diff_check = 0
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_count += 1
                if diff_count > 2:
                    return False
                if diff_count == 2:
                    if s[diff_check] == goal[i] and s[i] == goal[diff_check]:
                        diff_check = -1
                else:
                    diff_check = i

            alpha_count[ord(s[i]) - ord('a')] += 1
        
        if diff_count == 0:
            if max(alpha_count) >= 2:
                return True
        elif diff_count == 2:
            if diff_check == -1:
                return True
        
        return False
        