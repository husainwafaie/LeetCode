class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 1
        word = s[0]
        dct = {}
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = [i]
            else:
                for k in dct[s[i]]:
                    if s[k:i+1] == s[k:i+1][::-1] and len(s[k:i+1]) > count:
                        word = s[k:i+1]
                        count = len(word) 
                dct[s[i]].append(i)   
        return word