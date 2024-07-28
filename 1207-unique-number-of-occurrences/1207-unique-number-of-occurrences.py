class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct ={}
        for i in arr:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        s = set()
        for i in dct.keys():
            if dct[i] in s:
                return False
            s.add(dct[i])
        return True
        