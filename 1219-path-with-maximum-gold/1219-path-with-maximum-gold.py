class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, total):
            final = total
            steps = [[-1,0], [1, 0], [0,1], [0,-1]]
            for i, k in steps:
                x1 = x + i
                y1 = y + k
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] > 0:
                    temp = grid[x][y]
                    grid[x][y] = 0
                    final = max(final, dfs(x1, y1, total + grid[x1][y1]))
                    grid[x][y] = temp
            return final
        def check(x, y):
            steps = [[-1,0], [1, 0], [0,1], [0,-1]]
            for i, k in steps:
                x1 = x + i
                y1 = y + k
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1] > grid[x][y]:
                    return False
            return True

        longest = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                longest = max(longest, dfs(i, k, grid[i][k]))
        return longest