class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def add(s):
            num1 = s.pop()
            num2 = s.pop()
            s.append(num1 + num2)
        def sub(s):
            num = s.pop()
            num2 = s.pop()
            s.append(num2 - num)
        def mult(s):
            num = s.pop()
            num2 = s.pop()
            s.append(num * num2)
        def div(s):
            num1 = s.pop()
            num2 = s.pop()
            num = int(num2 / num1)
            s.append(num)

        dct = {
            "+":add,
            "-":sub,
            "*":mult,
            "/":div
        }
        for i in tokens:
            if i.isdigit() or (len(i) > 1 and i[0] == "-" and i[1:].isdigit()):
                stack.append(int(i))
            else:
                dct[i](stack)
        return stack[0]