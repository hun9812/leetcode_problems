class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        check1 = True
        check2 = True
        if points[0] == points[1]:
            return False
        if points[1] == points[2]:
            return False
        if points[0] == points[2]:
            return False



        if (points[0][1] - points[1][1]) != 0:
            der1 = (points[0][0] - points[1][0]) / (points[0][1] - points[1][1])
        else:
            check1 = False
        if (points[1][1] - points[2][1]) != 0:
            der2 = (points[1][0] - points[2][0]) / (points[1][1] - points[2][1])
        else: check2 = False

        if not check1 or not check2:
            if not check1 and not check2:
                return False
            return True

        if der1 == der2:
            return False
        else:
            return True
        