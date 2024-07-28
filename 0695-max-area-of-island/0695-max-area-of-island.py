class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        def dfs(num, x, y):
            if x + 1 < len(grid) and grid[x+1][y] == 1:
                grid[x+1][y] = 0
                num = dfs(num+1, x+1, y)
            if x - 1 >= 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 0
                num = dfs(num+1, x-1, y)
            if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
                grid[x][y+1] = 0
                num = dfs(num+1, x, y+1)
            if y - 1 >= 0 and grid[x][y-1] == 1:
                grid[x][y-1] = 0
                num = dfs(num+1, x, y-1)
            return num
        
        ret = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 1:
                    grid[i][k] = 0
                    n = dfs(1, i,  k)
                    if n > ret:
                        ret = n
        return ret