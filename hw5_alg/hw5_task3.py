from random import randint
from collections import deque
from timeit import timeit


# заполнение через append
def append_to(struct):
    for i in range(1000):
        struct.append(randint(0, 10))
    return struct


arr = []
deq = deque()
print(timeit('append_to(arr)', globals=globals(), number=10000))  # 10.104571279
print(timeit('append_to(deq)', globals=globals(), number=10000))  # 10.191440404
# вставка посредством append дает примерно одинаковое время для дека и для списка.
# Вставка в список даже чуть-чуть быстрее  на ~ 1%


# удаление через pop
def pop_from(struct):
    for i in range(1000):
        struct.pop()
    return struct


print(timeit('pop_from(arr)', globals=globals(), number=10000))  # 0.645689
print(timeit('pop_from(deq)', globals=globals(), number=10000))  # 0.677251
# методом pop список очищается быстрее на 1-5%


# рассмотрим метод extend
def extend_to(struct):
    for i in range(1000):
        struct.extend([randint(0, 10), randint(0, 10)])
    return struct


print(timeit('extend_to(arr)', globals=globals(), number=10000))  # 22.395
print(timeit('extend_to(deq)', globals=globals(), number=10000))  # 23.158
# методом extend  список заполняется быстрее на 2-5 %
# Таким образом, методы append, pop, extend работают чуть быстрее для списков.
# Это экспериментально полученный результат, хотя согласно теории времена у измерений должны
# быть одинаковые, т к дек наследует интерфейс списка. В рамках погрешности можем сказать,
# что они равны.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Начнем сравнение методов списка и дека
# insert и appendleft
def insert_into_list_to_start(array: list):
    for i in range(100):
        array.insert(0, randint(0, 10))
        # print(array)
    return array


def insert_into_deque_to_start(my_deque: deque):
    for i in range(100):
        my_deque.appendleft(randint(0, 10))
    return my_deque


print(timeit('insert_into_list_to_start(arr)', globals=globals(), number=1000))  # 2.495
print(timeit('insert_into_deque_to_start(deq)', globals=globals(), number=1000))  # 0.101


# Различия в 25 раз в пользу дека, что объясняется константой сложностью операции appendleft
# по сравнению с линейной для insert


# сравним pop и popleft
def pop_from_the_left_from_arr(array: list):
    for i in range(100):
        array.pop(0)
    return array


def pop_from_the_left_from_deque(my_deq: deque):
    for i in range(100):
        my_deq.popleft()
    return deq


print(timeit('pop_from_the_left_from_arr(arr)', globals=globals(), number=1000))  # 1.1674
print(timeit('pop_from_the_left_from_deque(deq)', globals=globals(), number=1000))  # 0.0058
# Различия на 3 порядка величины в пользу дека.


# extend и extendleft
def extend_into_arr(array: list):
    for i in range(100):
        array.extend([randint(0, 10), randint(0, 10)])
    return array


def extend_into_arr_to_the_left(my_deq: deque):
    for i in range(100):
        my_deq.extendleft([randint(0, 10), randint(0, 10)])
    return my_deq


print(timeit('extend_into_arr(arr)', globals=globals(), number=1000))  # 0.218
print(timeit('extend_into_arr_to_the_left(deq)', globals=globals(), number=1000))  # 0.219
# Время одинаковое, но невозможно вставить через extend в начало списка

# Таким образом, когда есть необходимость вставки элемента в начало списка, то дек позволяет
# сделать выигрыш во времени в несколько раз.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Сравним скорость получения элемента из списка и дека
def get_element(struct):
    return [struct[i] for i in range(len(struct))]


print(timeit('get_element(arr)', globals=globals(), number=100))  # 0.0643
print(timeit('get_element(deq)', globals=globals(), number=100))  # 0.120
# Получение элемента быстрее через список
