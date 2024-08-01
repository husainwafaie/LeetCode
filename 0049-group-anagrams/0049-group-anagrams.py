class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = 0
        dct = {}
        lst = []
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s in dct:
                lst[dct[s]].append(strs[i])
            else:
                dct[s] = count
                lst.append([strs[i]])
                count += 1
        return lst
        