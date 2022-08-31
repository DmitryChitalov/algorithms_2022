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


print('Append')
print(timeit("append_list()", globals=globals(), number=1000))
print(timeit("append_deque()", globals=globals(), number=1000))
print('Extend')
print(timeit("extend_list([500, 600, 700])", globals=globals(), number=10000))
print(timeit("extend_deque([500, 600, 700])", globals=globals(), number=10000))
print('insert & __left')
print(timeit("insert_list(532)", globals=globals(), number=10000))
print(timeit("insert_deque(532)", globals=globals(), number=10000))
print(timeit("appendleft_deque(532)", globals=globals(), number=10000))
print(timeit("extendleft_deque([500, 600, 700])",
      globals=globals(), number=10000))
print('Pop')
print(timeit("pop_list()", globals=globals(), number=10000))
print(timeit("pop_deque()", globals=globals(), number=10000))
print('Remove')
print(timeit("remove_list(25)", globals=globals(), number=1))
print(timeit("remove_deque(100)", globals=globals(), number=1))
print('Count')
print(timeit("count_list(500)", globals=globals(), number=10000))
print(timeit("count_deque(500)", globals=globals(), number=10000))
print('Get')
print(timeit("get_el_list(400)", globals=globals(), number=10000))
print(timeit("get_el_deque(400)", globals=globals(), number=10000))

"""
Append
list - 0.0008581000000000005
deque - 0.0010246000000000005
Extend
list - 0.0013018000000000057
deque - 0.0020106000000000013
insert & __left
list insert 0 - 0.16060839999999998
deque insert 0 - 0.0012784000000000129
appendleft - 0.0010721999999999954
extendleft - 0.001669799999999999
Pop
list - 0.0007618000000000069
deque - 0.0017931000000000197
Remove
list - 0.00013759999999998773
deque - 0.0010758999999999908
Count
list - 3.6429708
deque - 7.172634500000001
Get
list - 0.8913490999999993
deque - 4.222082

Добавление и расширение происходит на разных размерах практически одинаково +-
Добавление элемента по индексу происходит быстрее в очереди, так же appendleft работает быстрее чем добавление по индексу в начало списка
Удаление происходит немного быстрее в списках.
Получение элемента по индексу и подсчет элементов, происходит намного быстрее в списках
"""
