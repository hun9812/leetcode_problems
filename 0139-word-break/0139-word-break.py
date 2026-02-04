class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def can_find(k):
            if k == len(s):
                return True
            if k in memo:
                return memo[k]
            
            for i in range(k, len(s)):
                cur_word =  s[k:i+1]
                if cur_word in word_set:
                    if can_find(i+1):
                        memo[k] = True
                        return True
            memo[k] = False
            return False
        
        return can_find(0)