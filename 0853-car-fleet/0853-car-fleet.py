class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dct = {}
        for i in range(len(position)):
            dct[position[i]] = i
        position.sort()
        count = 0
        p = len(position) - 1
        while p >= 0:
            threshold = (target - position[p]) / speed[dct[position[p]]]
            while p - 1 >= 0 and ((target - position[p-1]) / speed[dct[position[p-1]]]) <= threshold:
                p -= 1
            p -= 1
            count += 1
        return count