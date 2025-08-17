# Условие: Касса в магазине (задачу генерил ГПТ)

# У тебя есть очередь из покупателей — список чисел, где каждое число — это время обслуживания одного клиента.
# У тебя только одна касса, она обслуживает по порядку.
# Напиши функцию total_wait_time(queue), которая вернёт общее время, которое потратят все люди в очереди, включая ожидание.


def total_wait_time(queue):
    total_time = 0
    current_time = 0
    
    for arrival, work in queue:
        if arrival <= current_time:
            total_time += current_time - arrival
            current_time += work
        else:
            current_time = arrival + work
    
    return total_time
