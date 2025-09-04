class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [arr[:] for arr in img]

        move = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]

        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 1
                val = img[i][j]
                for k in move:
                    try:
                        if i+k[0] < 0 or j+k[1] < 0 :
                            continue
                        val += img[i+k[0]][j+k[1]]
                        count += 1
                    except:
                        pass
                res[i][j] = val // count
        return res