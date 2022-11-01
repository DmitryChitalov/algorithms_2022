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
from random import randint
from collections import deque
from timeit import timeit

test_list = [randint(1, 1000) for x in range(100)]
test_dq = deque(test_list)


some_list = [x for x in range(100)]

"""
Первое задание.
Несмотря на то, что операции приведенные ниже имеют одинаковую сложность, для deque операции выполняются быстрее.
С ростом повторов выполнения растет и разница в процентах.
"""


def app_end(obj):
    for x in some_list:
        obj.append(x)
    return obj


def pop_el(obj):
    while len(obj) > 0:
        obj.pop()


def ex_tend(obj):
    obj.extend(some_list)
    return obj


print("Сначала замер для списка, потом для deque.")
print("append")
print(timeit("app_end(test_list)", "from __main__ import app_end, test_list", number=100000))
print(timeit("app_end(test_dq)", "from __main__ import app_end, test_dq", number=100000))
print("pop")
print(timeit("pop_el(test_list)", "from __main__ import pop_el, test_list", number=100000))
print(timeit("pop_el(test_dq)", "from __main__ import pop_el, test_dq", number=100000))
print("extend")
print(timeit("ex_tend(test_list)", "from __main__ import ex_tend, test_list", number=100000))
print(timeit("ex_tend(test_dq)", "from __main__ import ex_tend, test_dq", number=100000))

"""
Второе задание.
При выполнении операций appendleft(аналог для списка- insert(0)) и popleft(для списка - либо pop(0), либо del - время выполнения соразмерно), а также
edxtendleft(для списка та же операция, что и при добавлении поэлементно в начало, а deque выполняется быстрее, т.к. мы не проходим в цикле 
по элементам списка, а передаем методу список) сложность для list будет O(n), а для deque - O(1)
Пришлось снизить количество вызовов функции, иначе для list было очень долго ждать результатов

"""

test_list = [randint(1, 1000) for x in range(100)]
test_dq = deque(test_list)


def app_end_left(obj):
    if type(obj) == list:
        for x in some_list:
            obj.insert(0, x)
        return obj
    elif type(obj) == deque:
        for x in some_list:
            obj.appendleft(x)
        return obj


def pop_left(obj):
    if type(obj) == list:
        for i in obj:
            obj.pop(0)
    elif type(obj) == deque:
        while len(obj) > 0:
            obj.popleft()


def ex_tend_left(obj):
    if type(obj) == list:
        for x in some_list:
            obj.insert(0, x)
        return obj
    if type(obj) == deque:
        obj.extendleft(some_list)
        return obj


print("Сначала замер для списка, потом для deque.")
print("appendleft")
print(timeit("app_end_left(test_list)", "from __main__ import app_end_left, test_list", number=1000))
print(timeit("app_end_left(test_dq)", "from __main__ import app_end_left, test_dq", number=1000))
print("popleft")
print(timeit("pop_left(test_list)", "from __main__ import pop_left, test_list", number=1000))
print(timeit("pop_left(test_dq)", "from __main__ import pop_left, test_dq", number=1000))
print("extendleft")
print(timeit("ex_tend_left(test_list)", "from __main__ import ex_tend_left, test_list", number=1000))
print(timeit("ex_tend_left(test_dq)", "from __main__ import ex_tend_left, test_dq", number=1000))


"""
Третье задание.
При получении элемнтов, списки быстрее, они больше предназначены для индексации, причем выяснил, что несмотря на то, что
deque индексируется, slice от него получить нельзя :)
"""


def take_el(obj):
    for i in obj:
        i
    return None

print("Сначала замер для списка, потом для deque.")
print("Получение элемента.")

print(timeit("take_el(test_list)", "from __main__ import take_el, test_list", number=10000))
print(timeit("take_el(test_dq)", "from __main__ import take_el, test_dq", number=10000))
