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
from collections import deque
from timeit import timeit

my_list = [i for i in range(10 ** 2)]

my_deque = deque([i for i in range(10 ** 2)])


def list_app(my_list):
    for i in range(10 ** 2):
        my_list.append(i ** 2)
    return my_list


def deque_app(my_deque):
    for i in range(10 ** 2):
        my_deque.append(i ** 2)
    return my_deque


print(timeit('list_app(my_list.copy())', globals=globals(), number=100))
print(timeit('deque_app(my_deque.copy())', globals=globals(), number=100))

# 8.938851199999998 - операция добавления в список
# 9.6380171 - операция добавления в дек
print()


def list_pop(my_list):
    for i in range(10 ** 1):
        my_list.pop(i)
    return my_list


def deque_pop(my_deque):
    for i in range(10 ** 1):
        my_deque.pop()
    return my_deque


print(timeit('list_pop(my_list.copy())', globals=globals(), number=100))
print(timeit('deque_pop(my_deque.copy())', globals=globals(), number=100))

# # 6.8766757 - операция удаления со списком
# # 9.743675000000001 - операция удаления с деком
print()


def extend_list(my_list):
    for i in range(1, 100):
        my_list.extend([i for i in range(10)])
    return my_list


def extend_deque(my_deque):
    for i in range(1, 100):
        my_deque.extend([i for i in range(10)])
    return my_deque


print(timeit('extend_list(my_list.copy())', globals=globals(), number=100))
print(timeit('extend_deque(my_deque.copy())', globals=globals(), number=100))

# 8.694315000000001 - операция добавления элементов списка в список
# 9.559676800000002 - операция добавления элементов списка в дек
print()

'''Операции append, extend списка работают быстрее чем те же операции дека, операция pop дека
быстрее операции pop списка'''


def append_left_list(my_list):
    for i in range(1, 10):
        my_list.insert(0, i)
    return my_list


def append_left_deque(my_deque):
    for i in range(1, 10):
        my_deque.appendleft(i)
    return my_deque


print(timeit('append_left_list(my_list.copy())', globals=globals(), number=100))
print(timeit('append_left_deque(my_deque.copy())', globals=globals(), number=100))

# 14.1092869 - операция добавления в начало списка
# 9.566205700000001 - операция добавления в начало дека
print()


def popleft_list(my_list):
    for i in range(1, 100):
        my_list.remove(my_list[0])
    return my_list


def popleft_deque(my_deque):
    for i in range(1, 100):
        my_deque.popleft()
    return my_deque


print(timeit('popleft_list(my_list.copy())', globals=globals(), number=100))
print(timeit('popleft_deque(my_deque.copy())', globals=globals(), number=100))
# 0.0012175999999999992 - удаление элемента с начала списка
# 0.0003611000000000031 - удаление элемента с начала дека
print()

'''Встроенные методы дека работают быстрее, чем операции выполняющие аналогичные действия списка'''
