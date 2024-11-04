class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for i in s:
            dct[i] = 1 + dct.get(i, 0)
        for i in range(len(s)):
            if dct[s[i]] == 1:
                return i
        return -1
