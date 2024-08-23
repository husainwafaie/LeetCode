class Solution:
    def longestPalindrome(self, s: str) -> str:
        dct = {}
        for i in range(len(s)):
            if s[i] in dct:
                dct[s[i]].append(i)
            else:
                dct[s[i]] = [i]
        count = 1
        word = s[0]
        for i in dct.keys():
            for k in range(len(dct[i])):
                for j in range(k+1, len(dct[i])):
                    if s[dct[i][k]:dct[i][j]+1] == s[dct[i][k]:dct[i][j]+1][::-1]:
                        if len(s[dct[i][k]:dct[i][j]+1]) > count:
                            word = s[dct[i][k]:dct[i][j]+1]
                            count = len(word)
        return word