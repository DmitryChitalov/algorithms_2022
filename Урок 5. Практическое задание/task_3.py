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


def list_append():
    my_list = list(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_list.append(i)
    return my_list


def deque_append():
    my_deque = deque(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_deque.append(i)
    return my_deque


def list_pop():
    my_list = list(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_list.pop()
    return my_list


def deque_pop():
    my_deque = deque(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_deque.pop()
    return my_deque


def list_extend():
    my_list = list(range(100))
    test_list = list(range(10))
    my_list.extend(test_list)
    return my_list


def deque_extend():
    my_deque = deque(range(100))
    test_list = list(range(10))
    my_deque.extend(test_list)
    return my_deque


"""при выполнении стандартных операций которые поддерживает список и дэк, обычный список выигрывает по скорости"""


def list_append_left():
    my_list = list(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_list.insert(0, i)
    return my_list


def deque_append_left():
    my_deque = deque(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_deque.appendleft(i)
    return my_deque


def list_pop_left():
    my_list = list(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_list.pop(0)
    return my_list


def deque_pop_left():
    my_deque = deque(range(100))
    test_list = list(range(10))
    for i in test_list:
        my_deque.popleft()
    return my_deque


def list_extend_left():
    my_list = list(range(100))
    test_list = list(range(10))
    test_list.extend(my_list)
    return my_list


def deque_extend_left():
    my_deque = deque(range(100))
    test_list = list(range(10))
    my_deque.extendleft(test_list)
    return my_deque


"""при выполнении операций которые список не поддерживает дэк выигрывает по скорости"""


def get_el_list():
    my_list = list(range(100))
    for i in range(len(my_list) + 1):
        return my_list[i]


def get_el_deque():
    my_deque = deque(range(100))
    for i in range(len(my_deque) + 1):
        return my_deque[i]


"""при полученнии элемента по инднксу дэк проигрывает по скорости"""


print(timeit('list_append()', globals=globals(), number=10000))
print(timeit('deque_append()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('list_pop()', globals=globals(), number=10000))
print(timeit('deque_pop()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('list_extend()', globals=globals(), number=10000))
print(timeit('deque_extend()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('list_append_left()', globals=globals(), number=10000))
print(timeit('deque_append_left()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('list_pop_left()', globals=globals(), number=10000))
print(timeit('deque_pop_left()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('list_extend_left()', globals=globals(), number=10000))
print(timeit('deque_extend_left()', globals=globals(), number=10000))
print('*' * 60)
print(timeit('get_el_list()', globals=globals(), number=10000))
print(timeit('get_el_deque()', globals=globals(), number=10000))
print('*' * 60)
