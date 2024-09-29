class Solution:
    def rotatedDigits(self, n: int) -> int:
        dct = {
            "1": "1",
            "0":"0",
            "8":"8",
            "2":"5",
            "5":"2",
            "6":"9",
            "9":"6"
        }

        count = 0
        for i in range(1, n + 1):
            i = str(i)
            num = ""
            for k in i:
                if k not in dct:
                    break
                num += dct[k]
            if len(num) != len(i):
                continue
            if num != i:
                count += 1
        return count