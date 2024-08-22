class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        total = 0
        vowels = ["a", "i", "e", "o", "u"]
        if k >= len(s):
            for i in s:
                #if i == "a" or i == "i" or i == "e" or i == "o" or i == "u":
                if i in vowels:
                    total += 1
            return total
        l = 0
        for i in range(k):
            #if s[i] == "a" or s[i] == "i" or s[i] == "e" or s[i] == "o" or s[i] == "u":
            if s[i] in vowels:
                total += 1
        final = total
        k -= 1
        while k != len(s) - 1:
            #if s[l] == "a" or s[l] == "i" or s[l] == "e" or s[l] == "o" or s[l] == "u":
            if s[l] in vowels:
                total -= 1
            #if s[k+1] == "a" or s[k+1] == "i" or s[k+1] == "e" or s[k+1] == "o" or s[k+1] == "u":
            if s[k+1] in vowels:
                total += 1
            l += 1
            k += 1
            if total > final:
                final = total
        return final
        