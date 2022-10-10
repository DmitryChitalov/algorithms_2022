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

lst = [i for i in range(69)]
deq = deque(lst)

# Часть 1: сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее


def lst_append():
    for i in range(69):
        lst.append(i)
    return lst


def deq_append():
    for i in range(69):
        deq.append(i)
    return deq


def lst_pop():
    for i in range(69):
        lst.pop()
    return lst


def deq_pop():
    for i in range(69):
        deq.pop()
    return deq


def lst_extend():
    for i in range(69):
        lst.extend([1, 2, 3])
    return lst


def deq_extend():
    for i in range(69):
        deq.extend([1, 2, 3])
    return deq


print('--------------Измеряем "append"--------------')
print('lst', timeit('lst_append()', globals=globals(), number=1000))
print('deq', timeit('deq_append()', globals=globals(), number=1000))
print('--------------Измеряем "pop"--------------')
print('lst', timeit('lst_pop()', globals=globals(), number=1000))
print('deq', timeit('deq_pop()', globals=globals(), number=1000))
print('--------------Измеряем "extend"--------------')
print('lst', timeit('lst_extend()', globals=globals(), number=1000))
print('deq', timeit('deq_extend()', globals=globals(), number=1000))

"""
Вердикт: время выполнения операций практически совпадает, дек немного быстрее, за исключением операции extend
"""


# Часть 2: сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


def lst_appendleft():
    for i in range(69):
        lst.insert(0, i)
    return lst


def deq_appendleft():
    for i in range(69):
        deq.appendleft(i)
    return deq


def lst_popleft():
    for i in range(1):
        lst.pop()
    return lst


def deq_popleft():
    for i in range(1):
        deq.popleft()
    return deq


def lst_extendleft():
    for i in range(699):
        lst.extend([1, 2, 3])
    return lst


def deq_extendleft():
    for i in range(699):
        deq.extendleft([1, 2, 3])
    return deq


print('--------------Измеряем "appendleft"--------------')
print('lst', timeit('lst_appendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_appendleft()', globals=globals(), number=1000))
print('--------------Измеряем "popleft"--------------')
print('lst', timeit('lst_popleft()', globals=globals(), number=1000))
print('deq', timeit('deq_popleft()', globals=globals(), number=1000))
print('--------------Измеряем "extend"--------------')
print('lst', timeit('lst_extendleft()', globals=globals(), number=1000))
print('deq', timeit('deq_extendleft()', globals=globals(), number=1000))

"""
Вердикт: время выполнения операций деком намного меньше, за исключением extend : тут цифры похожи, 
зато в appendleft разница очень заметна
"""


# Часть 3: сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее


def lst_index():
    for i in range(699):
        lst[i] = i
    return lst


def deq_index():
    for i in range(699):
        deq[i] = i
    return deq


print('--------------Измеряем "index"--------------')
print('lst', timeit('lst_index()', globals=globals(), number=1000))
print('deq', timeit('deq_index()', globals=globals(), number=1000))

"""
Вердикт: получение доступа к случайному элементу в списке немного быстрее.
"""