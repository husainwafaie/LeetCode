class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # n = sum(wall[0])
        # heap = []
        # dct = {}
        # for i in range(len(wall)):
        #     heapq.heappush(heap, [wall[i][0], i, 1])
        # ret = len(wall)
        # for i in range(1, n):
        #     count = 0
        #     while heap and heap[0][0] == i:
        #         item = heapq.heappop(heap)
        #         count += 1
        #         heapq.heappush(heap, [item[0] + wall[item[1]][item[2]], item[1], item[2] + 1]) 
        #     ret = min(ret, len(wall) - count)
        # return ret
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
            #ret = min(ret, len(wall) - dct[key])
        return ret
        
        