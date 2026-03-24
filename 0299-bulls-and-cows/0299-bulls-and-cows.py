class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        B = 0
        num_count = [0,0,0,0,0,0,0,0,0,0]
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                A += 1
            else:
                num_count[int(secret[i])] += 1
        
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if num_count[int(guess[i])] > 0:
                    B += 1
                    num_count[int(guess[i])] -= 1
        
        return f"{A}A{B}B"