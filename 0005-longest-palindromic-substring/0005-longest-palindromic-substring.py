class Solution:
    def longestPalindrome(self, s: str) -> str:
        rem = []
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        for i in d.values():
            for k in i[::-1][:-1]:
                for j in i[:-1]:
                    if k > j:
                        if s[j:k+1] == s[j:k+1][::-1]:
                            rem.append(s[j:k+1])
        try:
            return sorted(rem, key = lambda x:len(x))[-1]
        except:
            return s[0]