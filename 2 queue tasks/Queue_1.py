# Условие (задачу генерил ГПТ)
# Напиши класс MyQueue, в котором реализованы 2 метода:

# enqueue(i) — добавить элемент в очередь
# dequeue() — удалить и вернуть первый элемент из очереди

class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
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


def test_queue():
    q = Queue()
    assert q.size == 0 and q.head is None and q.tail is None
    
    q.enqueue(42)
    assert q.size == 1 and q.head.value == 42 and q.tail.value == 42
    assert q.dequeue() == 42
    assert q.size == 0 and q.head is None and q.tail is None

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size == 3 and q.head.value == 1 and q.tail.value == 3
    assert q.dequeue() == 1 and q.dequeue() == 2 and q.dequeue() == 3
    assert q.dequeue() is None
    
    q.enqueue(10)
    q.enqueue(20)
    assert q.dequeue() == 10
    q.enqueue(30)
    assert q.size == 2 and q.head.value == 20 and q.tail.value == 30
    assert q.dequeue() == 20 and q.dequeue() == 30


test_queue()
