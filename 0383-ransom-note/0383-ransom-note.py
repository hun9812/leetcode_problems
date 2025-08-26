class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_list = list(ransomNote)
        mag_list = list(magazine)
        ransom_set = set(ransom_list)
        
        for i in ransom_set:
            if ransom_list.count(i) <= mag_list.count(i):
                continue
            else:
                return False
        
        return True
        