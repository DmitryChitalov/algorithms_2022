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
from random import randint
from timeit import timeit

lst, deq, = [], deque()
size = 50000
g_l = [randint(10, 100000) for i in range(size)]  # список для extend
g_d = deque(g_l)  # deque для  extend

print('1. Cравниваем операции append, pop, extend списка и дека')
statements = [
    'for i in range(size): lst.append(i)', 'list append: ',
    'for el in range(size): deq.append(el)', 'deque append: ',
    'for _ in range(len(lst)): lst.pop()', 'list pop: ',
    'for _ in range(len(deq)): deq.pop()', 'deque pop: ',
    'lst.extend(g_l)', 'list extend: ',
    'deq.extend(g_d)', 'deque extend: '
]

[print(info, timeit(st, setup="from __main__ import g_l, g_d, lst, deq, size", number=1))
 for st, info in zip(statements[::2], statements[1::2])]

print(len(lst), len(deq))

print('2.Сравниваем операции appendleft, popleft, extendleft дека и соответствующих им операций списка')
statements1 = [
    'lst.extend(g_l[::-1]),lst.extend(g_l)', 'list.extend() from the left: ',
    'deq.extendleft(g_d)', 'deque.extendleft(): ',
    'for _ in range(size): lst.pop(0)', 'list.pop from the left:  ',
    'for _ in range(size): deq.popleft()', 'deque.popleft(): ',
    'for i in range(size): lst.insert(0,i)', 'list.append from the left: ',
    'for i in range(size): deq.appendleft(i)', 'deque.appendleft: '
]
lst.clear()
[print(info, timeit(st, setup="from __main__ import g_l, g_d, lst, deq, size", number=1))
 for st, info in zip(statements1[::2], statements1[1::2])]

print('3. сравниваем операции получения элемента списка и дека ')
statements2 = [
    '(lst[i] for i in range(size))', 'выборка  из list:  ',
    '(deq[i] for i in range(size))', 'выборка  из deque'
]
[print(info, timeit(st, setup="from __main__ import g_l, g_d, lst, deq, size", number=1000000))
 for st, info in zip(statements2[::2], statements2[1::2])]

"""
1. decue чуть лучше на операциях append, операции pop примерно равны, и на extend медленнее.
2. На операциях appendleft, popleft, extendleft дека и соответствующих им операций списка
безоговорочная победа deque над list. У них просто разная вычислительная сложность.
3. По операциям получения элемента списка и дека  незначительная победа deque.
"""
