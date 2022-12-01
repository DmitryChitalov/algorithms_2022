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
import timeit


list_1 = []
list_deq = deque(list_1)

# 1)


def func_1(listic, obj, num=0):
    if num == 0:
        return listic.append(obj)
    elif num == 1:
        return listic.pop()
    elif num == 2:
        return listic.extend(list(obj))


def func_2(list_dq, obj, num=0):
    if num == 0:
        return list_dq.append(obj)
    elif num == 1:
        return list_dq.pop()
    elif num == 2:
        return list_dq.extend(list(obj))


numb = 'asdf'
# print(f'list.append = {timeit.timeit("func_1(list_1, numb)", globals=globals(), number=1000)}')
# print(f'deque(list).append = {timeit.timeit("func_2(list_deq, numb)", globals=globals(), number=1000)}')
# print(f'list.pop = {timeit.timeit("func_1(list_1, numb, num=1)", globals=globals(), number=1000)}')
# print(f'deque(list).pop = {timeit.timeit("func_2(list_deq, numb, num=1)", globals=globals(), number=1000)}')
# print(f'list.extend = {timeit.timeit("func_1(list_1, numb, num=2)", globals=globals(), number=1000)}')
# print(f'deque(list).extend = {timeit.timeit("func_2(list_deq, numb, num=2)", globals=globals(), number=1000)}')
# Судя по результатам функции (append, pop, extend) в list и deque(list) работают одинаково.
# 2)


def func_3(listic, obj, num=0):
    if num == 0:
        return listic.insert(0, obj)
    elif num == 1:
        return listic.pop(0)
    elif num == 2:
        return [listic.insert(0, i) for i in list(obj)]


def func_4(list_dq, obj, num=0):
    if num == 0:
        return list_dq.appendleft(obj)
    elif num == 1:
        return list_dq.popleft()
    elif num == 2:
        return list_dq.extendleft(list(obj))


print(f'list."appendleft" = {timeit.timeit("func_3(list_1, numb)", globals=globals(), number=1000)}')
print(f'deque(list).appendleft = {timeit.timeit("func_4(list_deq, numb)", globals=globals(), number=1000)}')
print(f'list."pop" = {timeit.timeit("func_3(list_1, numb, num=1)", globals=globals(), number=1000)}')
print(f'deque(list).popleft = {timeit.timeit("func_4(list_deq, numb, num=1)", globals=globals(), number=1000)}')
print(f'list."extend" = {timeit.timeit("func_3(list_1, numb, num=2)", globals=globals(), number=1000)}')
print(f'deque(list).extendleft = {timeit.timeit("func_4(list_deq, numb, num=2)", globals=globals(), number=1000)}')
# Судя по результатам функции (appendleft, popleft, extendleft) в deque(list) работают значительно быстрее чем аналоги в list.
# 3)


def func_5(listic, num=0):
    if num == 0:
        for i in listic:
            if listic[1] == i:
                return i
    else:
        return listic[2]


print(f'list.получение элемента в цикле = {timeit.timeit("func_5(list_1)", globals=globals(), number=1000)}')
print(f'deque(list).получение элемента в цикле = {timeit.timeit("func_5(list_deq)", globals=globals(), number=1000)}')
print(f'list.получение элемента по индексу = {timeit.timeit("func_5(list_1, num=1)", globals=globals(), number=1000)}')
print(f'deque(list).получение элемента по индексу = {timeit.timeit("func_5(list_deq, num=1)", globals=globals(), number=1000)}')
# Судя по результатам, получение элементов в цикле и по индексу занимают одинаковое время в deque(list) и в list.
