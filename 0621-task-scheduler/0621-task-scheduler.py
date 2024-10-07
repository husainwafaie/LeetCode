class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dct = {}
        for i in tasks:
            dct[i] = 1 + dct.get(i, 0)
        heap = []
        for x,y in dct.items():
            heapq.heappush(heap, [0, -y, x])
        
        time = 0
        while len(heap) > 0:
            item = heapq.heappop(heap)
            time = max(time, item[0]) + 1
            item[0] = time + n
            item[1] += 1
            if item[1] != 0:
                heapq.heappush(heap, item)
            while heap and heap[0][0] < time:
                item = heapq.heappop(heap)
                item[0] = time
                heapq.heappush(heap, item)
        return time