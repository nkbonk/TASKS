'''
https://leetcode.com/problems/min-stack/description/
'''
#  Time: O(1)
#  Space: O(n)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
