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

import random

from collections import deque
from timeit import timeit

my_list = [random.randint(1, 1000) for i in range(100)]
my_deque = deque(my_list)

print('1)')
print(timeit('my_list.append(100)', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.append(100)', 'from __main__ import my_deque', number=1000))
# примерно одинаково

print(timeit('my_list.pop()', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.pop()', 'from __main__ import my_deque', number=1000))
# примерно одинаково

print(timeit('my_list.extend([1, 2, 3])', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.extend([1, 2, 3])', 'from __main__ import my_deque', number=1000))
# примерно одинаково

print('2)')
print(timeit('my_list.insert(0, 100)', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.appendleft(100)', 'from __main__ import my_deque', number=1000))
# в deque в 10 раз быстрее

print(timeit('my_list.pop(0)', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.popleft()', 'from __main__ import my_deque', number=1000))
# в deque в 10 раз быстрее

print(timeit('for i in [0, 1, 2]: my_list.insert(i, i)', 'from __main__ import my_list', number=1000))
print(timeit('my_deque.extendleft([1, 2, 3])', 'from __main__ import my_deque', number=1000))
# в deque в 100 раз быстрее

print('3)')
print(timeit('my_list[100]', 'from __main__ import my_list', number=1000))
print(timeit('my_deque[100]', 'from __main__ import my_deque', number=1000))
# из deque в 2 раза дольше
