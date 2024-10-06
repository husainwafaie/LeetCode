class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort()
        count = 0
        while len(pairs) > 0:
            base = (target - pairs[-1][0]) / pairs[-1][1]
            pairs.pop()
            while pairs and ((target - pairs[-1][0]) / pairs[-1][1]) <= base:
                pairs.pop()
            count += 1

        return count