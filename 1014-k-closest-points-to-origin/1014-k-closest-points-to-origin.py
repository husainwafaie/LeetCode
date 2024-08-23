class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #return sorted(points, key = lambda x:math.sqrt(math.pow(x[0],2) + math.pow(x[1],2)))[:k]
        heap = []
        for i in points:
            key = -(i[0]**2 + i[1]**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (key, i))
            else:
                heapq.heappush(heap, (key, i))
        return [i for (k,i) in heap]