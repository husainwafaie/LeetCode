class Solution:
    def reorganizeString(self, s: str) -> str:
        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        heap = []
        for i in dct.keys():
            heapq.heappush(heap, (-dct[i], i))
        s = ""
        while True:
            if len(heap) > 0:
                first = heapq.heappop(heap)
            else:
                return s
            if len(heap) > 0:
                second = heapq.heappop(heap)
            elif -first[0] > 1 or (len(s) > 0 and s[-1] == first[1]):
                return ""
            else:
                return s + first[1]
            s += first[1]
            s += second[1]
            if first[0] != -1:
                heapq.heappush(heap, (first[0]+1, first[1]))
            if second[0] != -1:
                heapq.heappush(heap, (second[0]+1, second[1]))
        