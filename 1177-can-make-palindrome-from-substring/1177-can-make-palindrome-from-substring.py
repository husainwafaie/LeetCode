class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        lst = []
        for i in queries:
            temp = s[i[0]:i[1]+1]
            dct = {}
            for k in temp:
                if k in dct:
                    dct[k] += 1
                else:
                    dct[k] = 1
            for k in dct.keys():
                dct[k] = dct[k] % 2
            total = sum(dct[k] for k in dct.keys())
            if total % 2 == 1:
                total -= 1
            if int((total/2) + 0.5) > i[2]:
                lst.append(False)
            else:
                lst.append(True)
        return lst