class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        cur_col = 0

        res = []

        for i in mat:
            for j in i:
                if cur_col == 0:
                    res.append([j])
                    cur_col += 1
                    if cur_col == c:
                        cur_col = 0
                else:
                    res[-1].append(j)
                    cur_col += 1
                    if cur_col == c:
                        cur_col = 0
        return res
        