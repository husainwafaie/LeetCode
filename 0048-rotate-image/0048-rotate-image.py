class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(int(len(matrix) / 2)):
            matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]
        
        i = 0
        while i < len(matrix):
            for k in range(len(matrix) - 1, i, -1):
                matrix[i][k], matrix[k][i] = matrix[k][i], matrix[i][k]
            i += 1
        return
        