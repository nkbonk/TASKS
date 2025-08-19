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


if __name__ == "__main__":
    print("ТЕСТИРОВАНИЕ ОЧЕРЕДИ")
    q = Queue()
    
    # Добавляем элементы
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Добавлены элементы: 1, 2, 3")
    
    # Проверяем размер
    print(f"Размер очереди: {q.size} (ожидается: 3)")
    
    # Извлекаем элементы
    print(f"Извлечен: {q.dequeue()} (ожидается: 1)")
    print(f"Извлечен: {q.dequeue()} (ожидается: 2)")
    
    # Проверяем размер после извлечения
    print(f"Размер очереди: {q.size} (ожидается: 1)")
    
    # Извлекаем последний элемент
    print(f"Извлечен: {q.dequeue()} (ожидается: 3)")
    
    # Проверяем пустую очередь
    print(f"Размер пустой очереди: {q.size} (ожидается: 0)")
    print(f"Извлечение из пустой: {q.dequeue()} (ожидается: None)")
    
    print("ТЕСТ ЗАВЕРШЕН")
