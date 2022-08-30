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


my_list = []
my_deque = deque()
test_num = 10 ** 5

# 1) #################################################
# append()
print('1)', '#' * 50)
print('#' * 15, "append()", '#' * 15, '\n')


def list_append(lst: list):
    """Добавление в конец списка"""
    for i in range(test_num):
        lst.append(i)


def deque_append(dq: deque):
    """Добавление в конец деки"""
    for i in range(test_num):
        dq.append(i)


print('list_append()')
print(timeit('list_append(my_list)', globals=globals(), number=1000))
print()
print('deque_append()')
print(timeit('deque_append(my_deque)', globals=globals(), number=1000))
print()


# pop()
print('#' * 15, "pop()", '#' * 15, '\n')


def list_pop(lst: list):
    """Извлечение элемента из конца списка"""
    for i in range(1000):
        lst.pop()


def deque_pop(dq: deque):
    """Извлечение элемента из конца деки"""
    for i in range(1000):
        dq.pop()


print('list_pop()')
print(timeit('list_pop(my_list)', globals=globals(), number=10000))
print()
print('deque_pop()')
print(timeit('deque_pop(my_deque)', globals=globals(), number=10000))
print()


# extend()
print('#' * 15, "extend()", '#' * 15, '\n')


def list_extend(lst: list):
    """Дополнение элементами в конце списка"""
    for i in range(test_num):
        lst.extend([1])


def deque_extend(dq: deque):
    """Дополнение элементами в конце деки"""
    for i in range(test_num):
        dq.extend([1])


print('list_extend()')
print(timeit('list_extend(my_list)', globals=globals(), number=100))
print()
print('deque_extend()')
print(timeit('deque_extend(my_deque)', globals=globals(), number=100))
print()

"""
Вывод. Добавление в конец, извлечение с конца - быстрее быстрее обрабатываются в деке.
Дополнение элементами в конце - быстрее список. 
"""

# 2) #################################################
# appendleft()
print('2)', '#' * 50)
print('#' * 15, "appendleft()", '#' * 15, '\n')


def list_insert(lst: list):
    """Вставка элементов в начало списка"""
    for i in range(10):
        lst.insert(0, i)


def deque_appendleft(dq: deque):
    """Вставка элементов в начало деки"""
    for i in range(10):
        dq.appendleft(i)


print('list_insert()')
print(timeit('list_insert(my_list)', globals=globals(), number=10))
print()
print('deque_appendleft()')
print(timeit('deque_appendleft(my_deque)', globals=globals(), number=10))
print()


# popleft()
print('#' * 15, "popleft()", '#' * 15, '\n')


def list_popleft(lst: list):
    """Извлечение элементов из начала списка"""
    for i in range(10):
        lst.pop(0)


def deque_popleft(dq: deque):
    """Извлечение элементов из начала деки"""
    for i in range(10):
        dq.popleft()


print('list_popleft()')
print(timeit('list_popleft(my_list)', globals=globals(), number=10))
print()
print('deque_popleft()')
print(timeit('deque_popleft(my_deque)', globals=globals(), number=10))
print()


# extendleft()
print('#' * 15, "extendleft()", '#' * 15, '\n')


def list_extendleft(lst: list):
    """Дополнение элементами вначале списка"""
    for i in range(10):
        lst.insert(0, [i])


def deque_extendleft(dq: deque):
    """Дополнение элементами вначале деки"""
    for i in range(10):
        dq.extendleft([i])


print('list_extendleft()')
print(timeit('list_extendleft(my_list)', globals=globals(), number=10))
print()
print('deque_extendleft()')
print(timeit('deque_extendleft(my_deque)', globals=globals(), number=10))
print()

"""
Вывод. Операции связанные с началом (вставка слева, извлечение слева,
дополнение элементами слева) значительно быстрее обрабатываются в деке. 
"""

# 3) #################################################
print('3)', '#' * 50)
print('#' * 15, "get element", '#' * 15, '\n')


def list_change(lst: list):
    """Изменение элементов в списке по индексу"""
    for i in range(1000):
        lst[i] = lst[i + 1]


def deque_change(dq: deque):
    """Изменение элементов в деке по индексу"""
    for i in range(1000):
        dq[i] = dq[i + 1]


print('list_change()')
print(timeit('list_change(my_list)', globals=globals(), number=10000))
print()
print('deque_change()')
print(timeit('deque_change(my_deque)', globals=globals(), number=10000))
print()

"""
Вывод. Доступ по индексу быстрее происходит в списке.
"""

"""Информация в документации соответствует действительности"""
