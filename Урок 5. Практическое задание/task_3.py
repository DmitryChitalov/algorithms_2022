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
from timeit import timeit
from collections import deque

lst = [i for i in range(10)]
deq = deque(i for i in range(10))
number = 5000


# append, pop, extend
def append_to_iter(x):
    for i in range(10):
        new_obj = x.append(0)
    return new_obj


def pop_iter(x):
    for i in range(10):
        new_obj = x.pop()
    return new_obj


def extend_iter(x):
    for i in range(10):
        new_obj = x.extend([1, 2, 3])
    return new_obj


# appendleft, popleft, extendleft дека и соответствующих им операций списка
def app_left(x):
    for i in range(10):
        new_obj = x.appendleft(0)
    return new_obj


def pop_left(x):
    for i in range(10):
        new_obj = x.popleft()
    return new_obj


def extend_left(x):
    for i in range(10):
        new_obj = x.extendleft([1, 2, 3])
    return new_obj


def insert_left(x):
    for i in range(10):
        new_obj = x.insert(0, 0)
    return new_obj


def pop_lst(x):
    for i in range(10):
        new_obj = x.pop(0)
    return new_obj


def extend_lst(x):
    new_obj = [1, 2, 3].extend(x)
    return new_obj


# операции получения элемента
def get_it(x):
    for i in range(10):
        obj = x[i]
        return obj


print('Append списком: ', timeit("append_to_iter(lst)", number=number, globals=globals()))
print('Append деком: ', timeit("append_to_iter(deq)", number=number, globals=globals()))
print('Pop списком: ', timeit("pop_iter(lst)", number=number, globals=globals()))
print('Pop деком: ', timeit("pop_iter(deq)", number=number, globals=globals()))
print('Extend списком: ', timeit("extend_iter(lst)", number=number, globals=globals()))
print('Extend деком: ', timeit("extend_iter(deq)", number=number, globals=globals()))
print('Вставка в начало списка: ', timeit("insert_left(lst)", number=number, globals=globals()))
print('Вставка в начало дека: ', timeit("app_left(deq)", number=number, globals=globals()))
print('Удаление первого элемента списка: ', timeit("pop_lst(lst)", number=number, globals=globals()))
print('Удаление первого элемента дека: ', timeit("pop_left(deq)", number=number, globals=globals()))
print('Расширение списка с начала: ', timeit("extend_lst(lst)", number=number, globals=globals()))
print('Расширение дека с начала: ', timeit("extend_left(deq)", number=number, globals=globals()))
print('Получение элемента списка: ', timeit("get_it(lst)", number=number, globals=globals()))
print('Получение элемента дека: ', timeit("get_it(deq)", number=number, globals=globals()))

# Deque имеет прреимущество по скорости по сравнению со списком.
# Особенно в операциях вставки элемента в начало, удаления первого элемента, а так же при расширениях
