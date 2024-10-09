class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rzero = False
        czero = False
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 0:
                    if i == 0:
                        rzero = True
                    if k == 0:
                        czero = True
                    matrix[0][k] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for k in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][k] == 0:
                    matrix[i][k] = 0
        if czero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if rzero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0