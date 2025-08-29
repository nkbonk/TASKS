'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
class Solution:
    #  Time/Space: O(n), один проход в любом случае будет
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    #  ГПТ подсказал, что нужно сюда флоат вставить, тогда заработает.
                    #  Я забил в хабитику проверить это завтра, потому что сейчас оперативки в голове не хватает, чтобы все это обработать    :3
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
        return stack[-1]
