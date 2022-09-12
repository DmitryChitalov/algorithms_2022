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

import collections
from timeit import timeit


obj_list = [i for i in range(1000)]
obj_deque = collections.deque(
    [i for i in range(1000)])


# добавление элемента
def append_list():
    for i in range(10):
        obj_list.append(i)
    return obj_list


def append_deque():
    for i in range(10):
        obj_deque.append(i)
    return obj_deque


def extend_list(n):
    obj_list.extend(n)


def extend_deque(n):
    obj_deque.extend(n)


def insert_list(n):
    obj_list.insert(0, n)
    return obj_list


def insert_deque(n):
    obj_deque.insert(0, n)


def appendleft_deque(n):
    obj_deque.appendleft(n)
    return obj_deque


def extendleft_deque(n):
    obj_deque.extendleft(n)


# Удаление элемента
def pop_list():
    return obj_list.pop()


def pop_deque():
    return obj_deque.pop()


def remove_list(n):
    return obj_list.remove(n)


def remove_deque(n):
    return obj_deque.remove(n)


#  Подсчет кол-ва элементов
def count_list(n):
    return obj_list.count(n)


def count_deque(n):
    return obj_deque.count(n)


# получение объекта
def get_el_list(n):
    return obj_list.index(n)


def get_el_deque(n):
    return obj_deque.index(n)


print('- > Append')
print('list: ', timeit("append_list()", globals=globals(), number=1000))
print('deque: ', timeit("append_deque()", globals=globals(), number=1000))

print('- > Extend')
print('list: ', timeit("extend_list([500, 600, 700])", globals=globals(), number=10000))
print('deque: ', timeit("extend_deque([500, 600, 700])", globals=globals(), number=10000))

print('- > Insert / Appendleft / Extendleft')
print('list: ', timeit("insert_list(532)", globals=globals(), number=10000))
print('deque: ', timeit("insert_deque(532)", globals=globals(), number=10000))
print('deque (appendleft): ', timeit("appendleft_deque(532)", globals=globals(), number=10000))
print('deque (extendleft):', timeit("extendleft_deque([500, 600, 700])", globals=globals(), number=10000))

print('- > Pop')
print('list: ', timeit("pop_list()", globals=globals(), number=10000))
print('deque: ', timeit("pop_deque()", globals=globals(), number=10000))

print('- > Remove')
print('list: ', timeit("remove_list(25)", globals=globals(), number=1))
print('deque: ', timeit("remove_deque(100)", globals=globals(), number=1))

print('- > Count')
print('list: ', timeit("count_list(500)", globals=globals(), number=10000))
print('deque: ', timeit("count_deque(500)", globals=globals(), number=10000))

print('- > Get')
print('list: ', timeit("get_el_list(400)", globals=globals(), number=10000))
print('deque: ', timeit("get_el_deque(400)", globals=globals(), number=10000))

"""
- > Append
list:  0.0012317000000000022
deque:  0.0012494000000000116
- > Extend
list:  0.0034662000000000026
deque:  0.0025664999999999993
- > Insert / Appendleft / Extendleft
list:  0.32104299999999997
deque:  0.0026526999999999523
deque (appendleft):  0.0017809000000000297
deque (extendleft): 0.002762600000000004
- > Pop
list:  0.001181500000000002
deque:  0.0011781000000000152
- > Remove
list:  0.00017179999999999973
deque:  0.0012905000000000277
- > Count
list:  8.8188841
deque:  18.4102489
- > Get
list:  1.9801512999999993
deque:  11.474933000000004

Скорость большинства операций у list и deque примерно равна (Есть погрешности, но не значительные).
Основные различия проявляются в:
1. Добавление элемента по индексу - deque чуть быстрее; 
2. Получение элемента по индексу - deque быстрей; 
3. Подсчёт элементом - deque быстрей.
"""