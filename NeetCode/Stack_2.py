class MinStack:
    #  Все действия: O(1)
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        current_min = value if not self.stack else min(value, self.stack[-1][1])
        self.stack.append((value, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
