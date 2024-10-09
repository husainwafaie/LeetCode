class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        lp = [0] * 26
        ls = [0] * 26
        for i in range(len(p)):
            lp[ord(p[i]) - ord('a')] += 1
            ls[ord(s[i]) - ord('a')] += 1
        count = [0] if lp == ls else []
        for i in range(len(p), len(s)):
            ls[ord(s[i - len(p)]) - ord('a')] -= 1
            ls[ord(s[i]) - ord('a')] += 1
            if lp == ls:
                count.append(i - len(p) + 1)
        return count