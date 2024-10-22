class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        can = set()
        tail = set()
        for x, y in paths:
            can.add(x)
            tail.add(y)
        for i in tail:
            if i not in can:
                return i