class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        grid = []
        for i in range(len(matrix)):
            l = []
            for k in range(len(matrix[0])):
                l.append(-1)
            grid.append(l)

        def dfs(x, y):
            steps = [(-1, 0), (1,0), (0, 1), (0, -1)]
            longest = 0
            for i in steps:
                x1 = x + i[0]
                y1 = y + i[1]
                if 0 <= x1 < len(matrix) and 0 <= y1 < len(matrix[0]) and matrix[x1][y1] > matrix[x][y]:
                    if grid[x1][y1] == -1:
                        dfs(x1, y1)
                    if grid[x1][y1] >= longest:
                        longest = grid[x1][y1] + 1
            grid[x][y] = longest
            return
        longest = 0
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                dfs(i, k)
                if grid[i][k] > longest:
                    longest = grid[i][k]
        return longest + 1