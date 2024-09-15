class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #heap = []
        dct = {}
        for i in words:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        # for x,y in dct.items():
        #     if len(heap) == k:
        #         heapq.heappushpop(heap, ([y, x], x))
        #     else:
        #         heapq.heappush(heap, ([y, x], x))
        
        #heap = sorted(heap, key=lambda x:(-x[0][0], x[0][1]))
        lst = [[x,y] for x,y in dct.items()]
        lst = sorted(lst, key=lambda x:(-x[1], x[0]))[:k]
        
        return [x[0] for x in lst]