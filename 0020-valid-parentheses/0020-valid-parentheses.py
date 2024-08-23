class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        lst = []
        for i in s:
            if i in dct:
                lst.append(dct[i])
            else:
                if len(lst) > 0 and i == lst[-1]:
                    lst.pop()
                else:
                    return False
        if len(lst) == 0:
            return True
        return False