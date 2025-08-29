'''
https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
    #  все в сумме O(n), тут много скобок надо проверять, поэтому меньше не выйдет
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {'(' : ')', '[' : ']', '{' : '}'}
        closers = {')', ']', '}'}
        stack = []

        for bracket in s:
            if bracket in pairs:
                stack.append(pairs[bracket])
            elif bracket in closers:
                if not stack or stack[-1] != bracket:
                    return False
                stack.pop()
            else:
                return False

        return not stack
