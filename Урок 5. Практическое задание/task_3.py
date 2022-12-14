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

n = 100
test_list = [i ** 2 for i in range(1000)]
test_deque = deque([i ** 2 for i in range(1000)])


def list_append(test_list):
    for i in range(n):
        test_list.append(i)
    return test_list


def deque_append(test_deque):
    for i in range(n):
        test_deque.append(i)
    return test_deque


def list_pop(test_list):
    for i in range(n):
        test_list.pop()
    return test_list


def deque_pop(test_deque):
    for i in range(n):
        test_deque.pop()
    return test_deque


def list_extend(test_list):
    for i in range(n):
        test_list.extend(str(i))
    return test_list


def deque_extend(test_deque):
    for i in range(n):
        test_deque.extend(str(i))
    return test_deque


print('List операция append: ', timeit('list_append(test_list)', globals=globals(), number=1000))
print('Deque операция append: ', timeit('deque_append(test_deque)', globals=globals(), number=1000))
print('List операция pop: ', timeit('list_pop(test_list)', globals=globals(), number=1000))
print('Deque операция pop: ', timeit('deque_pop(test_deque)', globals=globals(), number=1000))
print('List операция extend: ', timeit('list_extend(test_list)', globals=globals(), number=1000))
print('Deque операция extend: ', timeit('deque_extend(test_deque)', globals=globals(), number=1000))


def list_appendleft(test_list):
    for i in range(n):
        test_list.insert(0, i)
    return test_list


def deque_appendleft(test_deque):
    for i in range(n):
        test_deque.appendleft(i)
    return test_deque


def list_popleft(test_list):
    for i in range(n):
        test_list = test_list[1:]
    return test_list


def deque_popleft(test_deque):
    for i in range(n):
        test_deque.popleft()
    return test_deque


def list_extendleft(test_list):
    for i in range(n):
        test_list.insert(0, str(i))
    return test_list


def deque_extendleft(test_deque):
    for i in range(n):
        test_deque.extendleft(str(i))
    return test_deque


print('List операция appendleft: ', timeit('list_appendleft(test_list)', globals=globals(), number=1000))
print('Deque операция appendleft: ', timeit('deque_appendleft(test_deque)', globals=globals(), number=1000))
print('List операция popleft: ', timeit('list_popleft(test_list)', globals=globals(), number=1000))
print('Deque операция popleft: ', timeit('deque_popleft(test_deque)', globals=globals(), number=1000))
print('List операция extendleft: ', timeit('list_extendleft(test_list)', globals=globals(), number=1000))
print('Deque операция extendleft: ', timeit('deque_extendleft(test_deque)', globals=globals(), number=1000))


def list_get_elm(test_list):
    for i in range(n):
        a = test_list[i]
    return test_list


def deque_get_elm(test_deque):
    for i in range(n):
        a = test_deque[i]
    return test_deque


print('List операция поиск элемента: ', timeit('list_get_elm(test_list)', globals=globals(), number=1000))
print('Deque операция поиск элемента: ', timeit('deque_get_elm(test_deque)', globals=globals(), number=1000))

"""
Вывод: Двустронний список выигрывает на порядок при операциях вначале списка,  при операциях в конце списка 
незначительно проигрывает методам для списка (при значительном уеличении n , пройгрышь по времени становится 
существенным). Извлечение элемента осуществляется быстрее

"""
