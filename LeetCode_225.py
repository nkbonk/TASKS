class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    # O(n)
    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1[0])
            self.queue1 = self.queue1[1:]
        self.queue1, self.queue2 = self.queue2, self.queue1

    # O(1)
    def pop(self):
        if not self.queue1:
            return -1
        result = self.queue1[0]
        self.queue1 = self.queue1[1:]
        return result

    # O(1)
    def top(self):
        return self.queue1[0] if self.queue1 else -1

    # O(1)
    def empty(self):
        return len(self.queue1) == 0
