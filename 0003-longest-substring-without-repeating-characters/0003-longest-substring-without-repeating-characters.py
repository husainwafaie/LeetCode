class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = 0
        prev = 0
        i = 0
        biggest = 0
        dct = {}
        while i < len(s):
            if s[i] in dct:
                if num > biggest:
                    biggest = num
                if dct[s[i]] >= prev:
                    prev = dct[s[i]] + 1
                    num = i - prev + 1
                else:
                    num += 1
                dct[s[i]] = i
            else:
                dct[s[i]] = i
                num += 1
            i += 1
        return max(biggest, num)


