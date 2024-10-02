class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        p = 0
        total = 0
        curr = ""
        while p != len(s):
            curr += s[p]
            if curr == "I":
                if p + 1 != len(s) and (s[p+1] == "V" or s[p+1] == "X"):
                    curr += s[p+1]
                    p += 1
            elif curr == "X":
                if p + 1 != len(s) and (s[p+1] == "L" or s[p+1] == "C"):
                    curr += s[p+1]
                    p += 1
            elif curr == "C":
                if p + 1 != len(s) and (s[p+1] == "D" or s[p+1] == "M"):
                    curr += s[p+1]
                    p += 1
            p += 1
            total += dct[curr]
            curr = ""
        return total