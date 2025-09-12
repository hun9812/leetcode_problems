class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        self.move = [[1,0], [0,1], [-1,0], [0,-1]]
        self.color = color
        self.target_color = image[sr][sc]
        if self.target_color == self.color:
            return image
        
        self.image[sr][sc] = color
        self.coloring(sr,sc)


        return self.image

    
    def coloring(self, sr, sc):
        for i in self.move:
            cur_sr = sr + i[0]
            cur_sc = sc + i[1]
            if cur_sr < 0 or cur_sc < 0:
                continue
            elif cur_sr >= len(self.image) or cur_sc >= len(self.image[0]):
                continue
            
            if self.image[cur_sr][cur_sc] == self.target_color:
                self.image[cur_sr][cur_sc] = self.color
                self.coloring(cur_sr,cur_sc)
        