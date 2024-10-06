class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        final = []
        def backtrack(stack, op, cl):
            if not op and not cl:
                final.append("".join(stack))
                return
            if op and op <= cl:
                stack.append("(")
                backtrack(stack, op - 1, cl)
                stack.pop()
            if not op or cl > op:
                stack.append(")")
                backtrack(stack, op, cl - 1)
                stack.pop()
        backtrack(stack, n, n)
        return final