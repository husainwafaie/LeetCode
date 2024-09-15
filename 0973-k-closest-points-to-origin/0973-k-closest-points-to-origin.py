class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            key = ((i[0] ** 2) + (i[1]**2)) ** 0.5
            if len(heap) == k:
                heapq.heappushpop(heap, (-key, i))
            else:
                heapq.heappush(heap, (-key, i))
        return [x[1] for x in heap]