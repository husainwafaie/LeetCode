class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dct = {}
        for i in range(len(wall)):
            total = 0
            for index in range(len(wall[i])):
                total += wall[i][index]
                if index != len(wall[i]) - 1:
                    dct[total] = 1 + dct.get(total, 0)
        ret = len(wall)
        for key in dct.keys():
            if len(wall) - dct[key] < ret:
                ret = len(wall) - dct[key]
        return ret
        
        