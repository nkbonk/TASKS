class Solution:
    #  O(n)
    def evalRPN(self, tokens):
        stack = []
        ops = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in ops:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            else:  
                stack.append(int(a / b))

        return stack[-1]
