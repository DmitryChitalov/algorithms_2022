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


def list_append():
    my_list = []
    for i in range(100):
        my_list.append(i)


def deque_append():
    my_deque = deque()
    for i in range(100):
        my_deque.append(i)


def list_pop():
    my_list = [i for i in range(100)]
    for i in range(100):
        my_list.pop()


def deque_pop():
    my_deque = deque([i for i in range(100)])
    for i in range(100):
        my_deque.pop()


def list_extend():
    my_list = []
    for i in range(100):
        my_list.extend([1])


def deque_extend():
    my_deque = deque()
    for i in range(100):
        my_deque.extend([1])


def list_append_left():
    my_list = []
    for i in range(100):
        my_list.insert(0, i)


def deque_append_left():
    my_deque = deque()
    for i in range(100):
        my_deque.appendleft(i)


def list_pop_left():
    my_list = [i for i in range(100)]
    for i in range(100):
        my_list.pop(0)


def deque_pop_left():
    my_deque = deque([i for i in range(100)])
    for i in range(100):
        my_deque.popleft()


def list_extend_left():
    my_list = []
    for i in range(100):
        my_list = [1] + my_list


def deque_extend_left():
    my_deque = deque()
    for i in range(100):
        my_deque.extendleft([1])


print("append test")
print(timeit("list_append()", setup="from __main__ import list_append", number=10000))
print(timeit("deque_append()", setup="from __main__ import deque_append", number=10000))
print("pop test")
print(timeit("list_pop()", setup="from __main__ import list_pop", number=10000))
print(timeit("deque_pop()", setup="from __main__ import deque_pop", number=10000))
print("extend test")
print(timeit("list_extend()", setup="from __main__ import list_extend", number=10000))
print(timeit("deque_extend()", setup="from __main__ import deque_extend", number=10000))

print("append left test")
print(timeit("list_append_left()", setup="from __main__ import list_append_left", number=10000))
print(timeit("deque_append_left()", setup="from __main__ import deque_append_left", number=10000))
print("pop left test")
print(timeit("list_pop_left()", setup="from __main__ import list_pop_left", number=10000))
print(timeit("deque_pop_left()", setup="from __main__ import deque_pop_left", number=10000))
print("extend left test")
print(timeit("list_extend_left()", setup="from __main__ import list_extend_left", number=10000))
print(timeit("deque_extend_left()", setup="from __main__ import deque_extend_left", number=10000))


"""
функции pop, append и extend для list и deque выполняются за одинаковое время
функции popleft, appendleft, extendleft для deque существенно быстрее чем аналоги для list
"""