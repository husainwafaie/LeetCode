class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(len(s)):
            p = i
            front = i + 1
            while 0 <= p < front < len(s):
                if s[p] == s[front]:
                    count += 1
                    p -= 1
                    front += 1
                else:
                    break
            p = i - 1
            front = i + 1
            while 0 <= p < front < len(s):
                if s[p] == s[front]:
                    count += 1
                    p -= 1
                    front += 1
                else:
                    break
        return count