class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        target = 0
        alice_sum = sum(aliceSizes)
        target = sum(bobSizes) + alice_sum
        alice_target = target//2 - alice_sum

        for i in aliceSizes:
            if i+alice_target in bobSizes:
                return [i, i+alice_target]
        
        return None
        