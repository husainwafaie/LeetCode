class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones) * -1
            stone2 = heapq.heappop(stones) * -1
            if stone1 == stone2:
                continue
            elif stone2 > stone1:
                stone = stone2 - stone1
            else:
                stone = stone1 - stone2
            heapq.heappush(stones, stone * -1)
        if len(stones) == 1:
            return stones[0] * -1
        return 0