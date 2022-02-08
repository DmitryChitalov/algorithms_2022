"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit


def array_append(c_array):
    for el in range(100):
        c_array.append(el)
    return c_array


def array_pop(c_array):
    for i in range(100):
        c_array.pop
    return c_array


def array_extend(c_array, p_array):
    c_array.extend(p_array)
    return c_array


def deque_appendleft(c_deque):
    for el in range(100):
        c_deque.appendleft(el)
    return c_deque


def deque_popleft(c_deque):
    for i in range(100):
        c_deque.popleft
    return c_deque


def deque_extendleft(c_deque, p_list):
    for i in range(100):
        c_deque.extendleft(p_list)
    return c_deque


def list_insert(c_list):
    for el in range(100):
        c_list.insert(0, el)
    return c_list


def list_popleft(c_list):
    for el in range(100):
        c_list.pop(0)
    return c_list


def list_extendleft(c_list, p_list):
    new_list = [c_list.reverse()]
    for el in range(100):
        new_list.extend(p_list)
    rez_list = [new_list.reverse()]
    return rez_list


my_list = []
my_deque = deque()
print(type(my_deque))

print('Append: ')
print(timeit("array_append(my_list)", globals=globals(), number=1000))                      # 0.006030399999999991
print(timeit("array_append(my_deque)", globals=globals(), number=1000))                     # 0.005982000000000015
print('Pop: ')
print(timeit("array_pop(my_list)", globals=globals(), number=1000))                         # 0.005427000000000001
print(timeit("array_pop(my_deque)", globals=globals(), number=1000))                        # 0.005595900000000001
print('Extend:')
print(timeit("array_extend(my_list, (1, 2))", globals=globals(), number=1000))              # 0.0007103999999999999
print(timeit("array_extend(my_deque, (1, 2))", globals=globals(), number=1000))             # 0.0007138000000000005
print('insert VS appendleft')
print(timeit("list_insert(my_list)", globals=globals(), number=1000))                       # 9.253777300000001
print(timeit("deque_appendleft(my_deque)", globals=globals(), number=1000))                 # 0.003470500000000598
print('pop[0] vs popleft')
print(timeit("list_popleft(my_list)", globals=globals(), number=1000))                      # 3.3506055000000003
print(timeit("deque_popleft(my_deque)", globals=globals(), number=1000))                    # 0.0036012999999996964
print('extend + reverse vs extendleft')
print(timeit("list_extendleft(my_list, (1, 2))", globals=globals(), number=1000))           # 0.036181299999999084
print(timeit("deque_extendleft(my_deque, (1, 2))", globals=globals(), number=1000))         # 0.0069806000000003365


# скорость выполнения операций append, pop и extend  одинаковая для списка и очереди
# скорость выполнения операций appendleft, popleft и extendleft для очереди значительно выше,
# чем скорость выполнения операций insert, pop[0] и extend c разворачиванием для списка
