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
        assert self.head is None and self.tail is None and self.size == 0
    
    # Сложность O(1) 
    def enqueue(self, i):
        new_node = QueueNode(i)
        assert new_node.value == i
        assert new_node.next is None
        if not self.tail:
            assert self.head is None
            self.head = new_node
            self.tail = new_node
        else:
            assert self.head is not None
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        # Эти (наверное) лишние, включить можно, но пока не обязательно
        # assert self.tail == new_node
        # assert self.tail.value == i
        # assert self.tail.next is None
        # assert self.size > 0

    # Сложность O(1)
    def dequeue(self):
        if not self.head:
            assert self.tail is None
            assert self.size == 0
            return None 
            
        old_head_value = self.head.value
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None

    # Сложность O(n)
    def check_integrity(self):
        if self.size == 0:
            assert self.head is None
            assert self.tail is None
        else:
            assert self.head is not None
            assert self.tail is not None
            assert self.tail.next is None
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next

# Финальные тест
def test_queue_integrity():
    q = Queue()
    q.check_integrity()
    q.enqueue(10)
    q.check_integrity()
    q.enqueue(20)
    q.check_integrity()
    q.enqueue(30)
    q.check_integrity()
    
    assert q.dequeue() == 10
    q.check_integrity()
    assert q.dequeue() == 20
    q.check_integrity()
    assert q.dequeue() == 30
    q.check_integrity()
    

# Запускаем тест
test_queue_integrity()
