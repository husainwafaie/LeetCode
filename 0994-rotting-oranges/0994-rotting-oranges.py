class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        start = []
        for i in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[i][k] == 1:
                    fresh += 1
                if grid[i][k] == 2:
                    start.append([i, k])
        
        def helper(lst):
            ret = []
            for x, y in lst:
                if x - 1 >= 0 and grid[x-1][y] == 1:
                    ret.append([x-1, y])
                    grid[x-1][y] = 2
                if x + 1 < len(grid) and grid[x+1][y] == 1:
                    ret.append([x+1, y])
                    grid[x+1][y] = 2
                if y - 1 >= 0 and grid[x][y-1] == 1:
                    ret.append([x, y-1])
                    grid[x][y-1] = 2
                if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
                    ret.append([x, y+1])
                    grid[x][y+1] = 2
            return ret

        minutes = 0
        while fresh != 0:
            minutes += 1
            coordinates = helper(start)
            if len(coordinates) == 0:
                return -1
            fresh -= len(coordinates)
            start = coordinates
        
        return minutes
        

