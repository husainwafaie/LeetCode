class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        s.add(tuple([0,0]))
        start = [0, 0]
        for i in path:
            if i == "N":
                start[0] += 1
            elif i == "S":
                start[0] -= 1
            elif i == "W":
                start[1] -= 1
            elif i == "E":
                start[1] += 1
            if tuple(start) in s:
                return True
            s.add(tuple(start))
        return False