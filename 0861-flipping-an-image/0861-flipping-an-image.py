class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            cur = image[i]
            # print(cur)
            cur = cur[::-1]
            for j in range(len(cur)):
                if cur[j] == 1:
                    cur[j] = 0
                else:
                    cur[j] = 1
            image[i] = cur
            
        return image
        