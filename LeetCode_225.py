class MyStack:
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)

        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))  # Допустимый урон
    
    def pop(self):
        return self.queue.pop(0) if self.queue else None  # Тоже допустимый урон с pop(0), не критично
    
    def top(self):
        return self.queue[0] if self.queue else None
    
    def empty(self):
        return len(self.queue) == 0
