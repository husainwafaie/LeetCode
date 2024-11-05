class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        heap = []
        for i in nums:
            dct[i] = 1 + dct.get(i, 0)
        for key, val in dct.items():
            heapq.heappush(heap, (-val, key))
        res = []
        while len(res) != k:
            res.append(heapq.heappop(heap)[1])
        return res