class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        def get(n):
            temp = str(n)
            ret = 0
            for i in temp:
                ret += int(i) ** 2
            return ret
        
        while n != 1:
            n = get(n)
            if n in found:
                return False
            found.add(n)
        return True