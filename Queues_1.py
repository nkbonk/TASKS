# Условие (задачу генерил ГПТ)
# Напиши класс MyQueue, в котором реализованы 2 метода:

# enqueue(x) — добавить элемент в очередь
# dequeue() — удалить и вернуть первый элемент из очереди

# Очередь должна работать по принципу FIFO.

class MyQueue:
    def __init__(self):
        self.q = []
        self.head = 0

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if self.head >= len(self.q):
            return None
        val = self.q[self.head]
        self.head += 1
        return val
