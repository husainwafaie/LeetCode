class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        if len(t) == 0:
            return True
        p = 0
        for i in range(len(s)):
            if s[i] == t[p]:
                if p == len(t) - 1:
                    return True
                p += 1
        return False