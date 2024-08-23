class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for i in s:
            if i in dct:
                stack.append(dct[i])
            else:
                if len(stack) > 0 and stack[-1] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True