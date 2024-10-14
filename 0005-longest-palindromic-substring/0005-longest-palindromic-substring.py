class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 1
        word = s[0]
        for i in range(len(s)):
            left, right = i - 1, i + 1
            while left>= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > longest:
                        longest = right - left + 1
                        word = s[left:right + 1]
                else:
                    break
                left -= 1
                right += 1
            left, right = i, i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > longest:
                        longest = right - left + 1
                        word = s[left:right + 1]
                else:
                    break
                left -= 1
                right += 1
        return word