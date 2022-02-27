"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

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
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from timeit import timeit
from collections import deque

just_list = [i for i in range(1000)]
just_deque = deque([i for i in range(1000)])

# ______________Операция append(добавление элементов) приблизительно равны


# Добавление элементов в список
# append_list ---- 0.07314499999999999
def append_list(my_list):
    for i in range(1000):
        my_list.append(i)
    return my_list


append_list(just_list.copy())


# Добавление элементов в дэк
# append_deque ---- 0.08143520000000001
def append_deque(my_deque):
    for i in range(1000):
        my_deque.append(i)
    return my_deque


append_deque(just_deque.copy())


# ______________Операция extend (добавление списка в конец, слияние) приблизительно равны

ex_list = [i for i in range(1000)]


# Операция extend
# extend_list ---- 0.01040060000000001
def extend_list(list_1, list_2):
    list_1.extend(list_2)
    return list_1


extend_list(just_list.copy(), ex_list.copy())


# Операция extend
# extend_deque ---- 0.024056599999999984
def extend_deque(deque_1, deque_2):
    deque_1.extend(deque_2)
    return deque_1


extend_deque(just_deque.copy(), ex_list.copy())

# ______________Операция pop (удаление элементов) приблизительно равно


# Удаление элементов в списке
# pop_list ---- 0.0672236
def pop_list(my_list):
    for _ in range(1000):
        my_list.pop()
    return my_list


pop_list(just_list.copy())


# удаление элементов в дэке
# pop_deque ---- 0.06577850000000002
def pop_deque(my_deque):
    for _ in range(1000):
        my_deque.pop()
    return my_deque


pop_deque(just_deque.copy())




print(f'append_list ---- {timeit("append_list(just_list.copy())", globals=globals(), number=1000)}')
print(f'append_deque ---- {timeit("append_deque(just_deque.copy())", globals=globals(), number=1000)}')

print(f'extend_list ---- {timeit("extend_list(just_list.copy(), ex_list.copy())", globals=globals(), number=1000)}')
print(f'extend_deque ---- {timeit("extend_deque(just_deque.copy(), ex_list.copy())", globals=globals(), number=1000)}')

print(f'pop_list ---- {timeit("pop_list(just_list.copy())", globals=globals(), number=1000)}')
print(f'pop_deque ---- {timeit("pop_deque(just_deque.copy())", globals=globals(), number=1000)}')