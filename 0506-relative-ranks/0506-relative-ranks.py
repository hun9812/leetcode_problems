class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        for_sort = score[:]
        for_sort.sort(reverse = True)
        

        for i in range(len(score)):
            for j in range(len(for_sort)):
                if score[i] == for_sort[j]:
                    score[i] = str(j+1)
                    break
        
        for i in range(len(score)):
            if score[i] == '1':
                score[i] = "Gold Medal"
        for i in range(len(score)):
            if score[i] == '2':
                score[i] = "Silver Medal"
        for i in range(len(score)):
            if score[i] == '3':
                score[i] = "Bronze Medal"
        
        return score
