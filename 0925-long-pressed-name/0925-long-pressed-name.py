class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        prev = name[0]
        check = False
        num_typed = 0
        
        for i in range(len(name)):
            if num_typed > len(typed) - 1:
                return False
            if name[i] == typed[num_typed]:
                num_typed += 1
                prev = name[i]
                continue
            else:
                while prev == typed[num_typed]:
                    num_typed += 1
                    if num_typed > len(typed) - 1:
                        return False
                if name[i] == typed[num_typed]:
                    num_typed += 1
                    prev = name[i]
                else:
                    return False
        

        while num_typed < len(typed) and prev == typed[num_typed]:
            num_typed += 1
        if num_typed != len(typed):
            return False

        return True
        