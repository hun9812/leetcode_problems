class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output_matrix[j][i] = matrix[i][j]

        return output_matrix 
        