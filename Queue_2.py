# Задачу генерил ГПТ

# В супермаркете работает самодельная система управления очередью к кассе. Каждый покупатель имеет корзину с товарами. 
# Когда покупатель приходит, он добавляется в очередь через команду arrive(n), где n — количество товаров в его корзине. 

# Существует команда process() — она обслуживает первого покупателя в очереди: если у него осталось больше одного товара, то система уменьшает количество товаров на один и он остаётся в очереди; если остался один товар, то после обслуживания он уходит из очереди. 
# Нужно реализовать класс CheckoutQueue, поддерживающий команды arrive(n), process() и queue_state(), возвращающий список текущего количества товаров у каждого покупателя в очереди. 

# Если очередь пуста и вызвана команда process(), метод должен вернуть False, иначе True.

class CheckoutQueue:
    def __init__(self):
        self.queue = []
        self.current = 0

    def arrive(self, n):
        self.queue.append(n)

    # Сложность: O(1)
    def process(self):
        if self.current >= len(self.queue):
            return False

        self.queue[self.current] -= 1        
        if self.queue[self.current] == 0:
            self.current += 1

        return True

    # Сложность: O(n)
    def queue_state(self):
        return self.queue[self.current:]


# Тесты, по сложности O(n) 
def test_checkout_queue():
    q = CheckoutQueue()
    q.arrive(3)
    q.arrive(2)
    q.arrive(1)
    assert q.queue_state() == [3, 2, 1]
    result = q.process()
    assert result == True
    assert q.queue_state() == [2, 2, 1]
    q.process()  # [1, 2, 1]
    q.process()  # [0, 2, 1]
    assert q.queue_state() == [2, 1]
    
    q2 = CheckoutQueue()
    result = q2.process()
    assert result == False
    assert q2.queue_state() == []
    
    q3 = CheckoutQueue()
    q3.arrive(1)
    q3.arrive(1)
    q3.arrive(2)
    q3.process()
    assert q3.queue_state() == [1, 2]
    q3.process()
    assert q3.queue_state() == [2]
    q3.process()
    assert q3.queue_state() == [1]
    
    q4 = CheckoutQueue()
    q4.arrive(5)
    q4.arrive(3)
    for _ in range(4):
        q4.process()
    assert q4.queue_state() == [1, 3]
    q4.process()
    assert q4.queue_state() == [3]

    q5 = CheckoutQueue()
    q5.arrive(1)
    assert q5.process() == True
    assert q5.queue_state() == []
    assert q5.process() == False


test_checkout_queue()
