class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def move(p):
            if p + len(needle) > len(haystack):
                return False
            for i in range(p, p + len(needle)):
                if haystack[i] != needle[i - p]:
                    return False
            return True

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if move(i):
                    return i
        return -1
                