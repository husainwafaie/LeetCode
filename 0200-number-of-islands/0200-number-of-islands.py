class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, k):
            if i - 1 > -1 and grid[i-1][k] == "1":
                grid[i-1][k] = "0"
                bfs(i-1, k)
            if i + 1 < len(grid) and grid[i+1][k] == "1":
                grid[i+1][k] = "0"
                bfs(i+1, k)
            if k - 1 > -1 and grid[i][k-1] == "1":
                grid[i][k-1] = "0"
                bfs(i, k-1)
            if k + 1 < len(grid[0]) and grid[i][k+1] == "1":
                grid[i][k+1] = "0"
                bfs(i, k+1)

        total = 0
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == "1":
                    total += 1
                    bfs(i, k)
        return total
        