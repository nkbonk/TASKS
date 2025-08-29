class MyStack:
    def __init__(self):
        self.q = [] 

    def push(self, x: int) -> None:
        self.q.append(x)
        #  O(n)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0)) 

    #  pop(0) — O(n)
    def pop(self) -> int:
        return self.q.pop(0)
    
    #  O(1)
    def top(self) -> int:
        return self.q[0]
    
    #  O(1)
    def empty(self) -> bool:
        return len(self.q) == 0
