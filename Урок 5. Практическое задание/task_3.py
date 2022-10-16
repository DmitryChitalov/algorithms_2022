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

a = [66, 33, 1, 123.5, 5]
simple_list = list('bcd')
deq_obj = deque(simple_list)
print(deq_obj)
print(a)
print('-' * 100)

a.append(333)
deq_obj.append('e')
print(deq_obj)
print(a)
print('-' * 100)

a.insert(0, 10.5)
deq_obj.appendleft('100')
print(deq_obj)
print(a)
print('-' * 100)

deq_obj.pop()
a.pop()
print(deq_obj)
print(a)
print('-' * 100)

deq_obj.popleft()
a.pop(0)
print(deq_obj)
print(a)
print('-' * 100)

deq_obj.extend(['5', '10'])
a.extend(['x', 'y'])
print(deq_obj)
print(a)
print('-' * 100)

deq_obj.extendleft(['A', 'B'])
a.insert(0, 100)
print(deq_obj)
print(a)
print('-' * 100)
