class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check(d):
            for i in d.keys():
                if d[i] > 0:
                    return False
            return True
        dct = {}
        for i in s1:
            dct[i] = 1 + dct.get(i, 0)
        l = 0
        for r in range(len(s2)):
            if s2[r] in dct:
                dct[s2[r]] -= 1
            if r - l + 1 == len(s1):
                if check(dct):
                    return True
                if s2[l] in dct:
                    dct[s2[l]] += 1
                l += 1
        return False