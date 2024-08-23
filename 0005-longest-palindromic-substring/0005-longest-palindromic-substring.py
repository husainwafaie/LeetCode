class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 1
        word = s[0]
        for i in range(len(s)):
            for k in range(i+1, len(s)):
                if s[i] == s[k] and s[i:k+1] == s[i:k+1][::-1] and len(s[i:k+1]) > count:
                    word = s[i:k+1]
                    count = len(word)
        return word