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
import random
from collections import deque
from timeit import timeit

"""1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""

some_lst = list(random.randint(0, 10000) for i in range(1000))
some_deque = deque(random.randint(0, 10000) for j in range(1000))


# append


def append_list(s_lst):
    for i in range(1, 100000):
        some_lst.append(i)
        return s_lst


def append_deque(s_deque):
    for i in range(1, 100000):
        some_deque.append(i)
        return s_deque


print('Время выполнения append')
print(timeit('append_list(some_lst)', globals=globals(), number=10000))
print(timeit('append_deque(some_deque)', globals=globals(), number=10000))


# pop


def pop_list(s_lst):
    for i in range(1, 100000):
        some_lst.pop()
        return s_lst


def pop_deque(s_deque):
    for i in range(0, 100000):
        some_deque.pop()
        return s_deque


print('Время выполнения pop')
print(timeit('pop_list(some_lst)', globals=globals(), number=10000))
print(timeit('pop_deque(some_deque)', globals=globals(), number=10000))


# extend


def extend_list(s_lst):
    for i in range(1, 100000):
        some_lst.extend([random.randint(100, 10000)])
        return s_lst


def extend_deque(s_deque):
    for i in range(1, 100000):
        some_deque.extend([random.randint(100, 10000)])
        return s_deque


print('Время выполнения extend')
print(timeit('extend_list(some_lst)', globals=globals(), number=10000))
print(timeit('extend_deque(some_deque)', globals=globals(), number=10000))

# Вывод: append, pop, extend списка и дека отработали за примерно одинаковое количество времени

"""2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""


# appendleft


def insert_list(s_lst):
    for i in range(1, 1000):
        some_lst.insert(0, i)
    return s_lst


def appendleft_deque(s_deque):
    for i in range(1, 1000):
        some_deque.appendleft(i)
    return s_deque

print('Время выполнения appendleft')
print(timeit('insert_list(some_lst)', globals=globals(), number=100))
print(timeit('appendleft_deque(some_deque)', globals=globals(), number=100))


# popleft


def popleft_list(s_lst):
    for i in range(1, 1000):
        some_lst.pop(i)
    return s_lst


def popleft_deque(s_deque):
    for i in range(1, 1000):
        some_deque.popleft()
    return s_deque


print('Время выполнения popleft')
print(timeit('popleft_list(some_lst)', globals=globals(), number=100))
print(timeit('popleft_deque(some_deque)', globals=globals(), number=100))


# extendleft


def extendleft_list(s_lst):
    for j in range(0, 100):
        some_lst.insert(0, [10, 20, 30])
    return s_lst


def extendleft_deque(s_deque):
    for j in range(0, 100):
        some_deque.extendleft([10, 20, 30])
    return s_deque

print('Время выполнения extendleft')
print(timeit('extendleft_list(some_lst)', globals=globals(), number=1000))
print(timeit('extendleft_deque(some_deque)', globals=globals(), number=1000))


# Вывод: время выполнения операций appendleft, popleft, extendleft дека значительно меньше

"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
"""
some_lst_i = list(random.randint(0, 10000) for i in range(1000))
some_deque_i = deque(random.randint(0, 10000) for j in range(1000))


def extraction_lst(n):
    for i in range(len(some_lst_i)):
        some_lst_i[i] = n
    return n


def extraction_deque(n):
    for i in range(len(some_deque_i)):
        some_deque_i[i] = n
    return n



print('Получение элементов')
print(timeit('extraction_lst(some_lst_i)', globals=globals(), number=100))
print(timeit('extraction_deque(some_deque_i)', globals=globals(), number=100))

# Вывод: скорость получения элемента списка по индексу быстрее
