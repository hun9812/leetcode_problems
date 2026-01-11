from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        total_combinations = 1
        for d in digits:
            total_combinations *= len(digit_dict[d])
        
        res = ["" for _ in range(total_combinations)]
        
        current_repeat_group = total_combinations
        for d in digits:
            letters = digit_dict[d]
            current_repeat_group //= len(letters)
            
            for i in range(total_combinations):
                char_idx = (i // current_repeat_group) % len(letters)
                res[i] += letters[char_idx]
        
        return res
        