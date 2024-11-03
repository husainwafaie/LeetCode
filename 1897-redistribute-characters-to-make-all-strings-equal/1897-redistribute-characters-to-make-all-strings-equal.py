class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dct = {}
        for i in range(len(words)):
            for k in range(len(words[i])):
                dct[words[i][k]] = 1 + dct.get(words[i][k], 0)
        for i in dct.keys():
            if dct[i] % len(words) != 0:
                return False
        return True