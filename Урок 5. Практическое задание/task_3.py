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

test_list = []
test_deque = deque()
lst_nums = [-30, 10, 11, 12, 13, 22, 77]


def app_list(n):
    test_list = []
    for i in range(len(n)):
        test_list.append(i)


def app_deque(n):
    test_deque = deque()
    for i in range(len(n)):
        test_deque.append(i)


print(timeit('app_list(lst_nums)', globals=globals()))
print(timeit('app_deque(lst_nums)', globals=globals()))
'''
Добавление в deque выполняется почти одинаково с  добавлением в list
'''


def insert_list(n):
    test_list = []
    for i in range(len(n)):
        test_list.insert(0, i)


def app_left_deque(n):
    test_deque = deque()
    for i in range(len(n)):
        test_deque.appendleft(i)


print(timeit('insert_list(lst_nums)', globals=globals()))
print(timeit('app_left_deque(lst_nums)', globals=globals()))

'''
Операция appendleft в deque выполняется быстрее операции insert в list
'''


def pop_list():
    n = [-30, 10, 11, 12, 13, 22, 77]
    n.pop()


def pop_deque():
    n = deque(lst_nums)
    n.pop()


def pop_list_0():
    n = [-30, 10, 11, 12, 13, 22, 77]
    n.pop(0)


def pop_deque_0():
    n = deque(lst_nums)
    n.popleft()


print(timeit('pop_list()', globals=globals()))
print(timeit('pop_deque()', globals=globals()))
print(timeit('pop_list_0()', globals=globals()))
print(timeit('pop_deque_0()', globals=globals()))

'''
Удаление первого и последнего элемента быстрее в deque
'''


def extend_list():
    n = [-30, 10, 11, 12, 13, 22, 77]
    n.extend([10, 9, 7])


def extend_deque():
    n = deque(lst_nums)
    n.extendleft([10, 9, 7])


print(timeit('extend_list()', globals=globals()))
print(timeit('extend_deque()', globals=globals()))

'''
Метод расширения list через extend занимает меньше времени чем расширение deque.
'''
