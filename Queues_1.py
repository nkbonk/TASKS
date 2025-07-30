# Условие (задачу генерил ГПТ)
# Напиши класс MyQueue, в котором реализованы 2 метода:

# enqueue(x) — добавить элемент в очередь
# dequeue() — удалить и вернуть первый элемент из очереди

# Очередь должна работать по принципу FIFO.

class MyQueue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)

    def dequeue(self):
        if not self.q:
            return None
        return self.q.pop(0)
