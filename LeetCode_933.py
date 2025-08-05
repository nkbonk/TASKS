    def __init__(self):
        self.calls = []
        self.left = 0 
    
    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[self.left] < t - 3000:
            self.left += 1
        return len(self.calls) - self.left
