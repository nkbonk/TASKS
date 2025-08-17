# Условие (задачу генерил ГПТ)
# Напиши класс MyQueue, в котором реализованы 2 метода:

# enqueue(i) — добавить элемент в очередь
# dequeue() — удалить и вернуть первый элемент из очереди

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, i):
        new_node = QueueNode(i)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if not self.head:
            return None 
            
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        
        return val
