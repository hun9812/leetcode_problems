class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        cur = False
        absent = 0
        for i in s:
            if i == "A":
                absent += 1
                cur = False
            elif i == "L":
                if cur:
                    late += 1
                    if late == 3:
                        return False
                else:
                    cur = True
                    late = 1
            else:
                cur = False
        
        if absent < 2:
            return True
        else:
            return False
        