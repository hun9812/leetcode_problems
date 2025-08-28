class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word:
            return True

        if word.upper() == word:
            return True
        
        if ord(word[0]) <= ord("Z"):
            for i in range(1, len(word)):
                if ord(word[i]) > ord("Z"):
                    continue
                else:
                    return False
            return True
        return False
        