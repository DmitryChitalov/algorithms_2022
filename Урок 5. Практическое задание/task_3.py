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

l = list()
d = deque()
extender = [i for i in range(101, 201)]

for i in range(100):
    l.append(i)

for i in range(100):
    d.append(i)

l.extend(extender)
d.extend(extender)

for i in range(100):
    l.pop(0)

for i in range(100):
    d.pop()

# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее

results_1 = {
    'list append': timeit('for i in range(100): l.append(i)', globals=globals(), number=1000),
    'deque append': timeit('for i in range(100): d.append(i)', globals=globals(), number=1000),
    'list extend': timeit('l.extend(extender)', globals=globals(), number=1000),
    'deque extend': timeit('d.extend(extender)', globals=globals(), number=1000),
    'list pop': timeit('l.pop()', globals=globals(), number=1000),
    'deque pop': timeit('d.pop()', globals=globals(), number=1000)

}

for k, v in results_1.items(): print(f'{k}: {v}')

print('-' * 100)
# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее


for i in range(100):
    l.insert(0, i)

for i in range(100):
    d.appendleft(i)

# for i in range(100):
#     l.pop(0)
#
# for i in range(100):
#     d.popleft()
#
# l = extender + l
# d.extendleft(extender)

results_2 = {
    'list insert': timeit('for i in range(100): l.insert(0, i)', globals=globals(), number=1000),
    'deque appendleft': timeit('for i in range(100): d.appendleft(i)', globals=globals(), number=1000),
    'list pop': timeit('for i in range(100): l.pop(0)', globals=globals(), number=1000),
    'deque popleft': timeit('for i in range(100): d.popleft()', globals=globals(), number=1000),
    'list extend left': timeit('l[0:0] = extender', globals=globals(), number=1000),
    'deque extendleft': timeit('d.extendleft(extender)', globals=globals(), number=1000)
}

for k, v in results_2.items(): print(f'{k}: {v}')

print('-' * 100)
# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

results_3 = {
    'list single_out': timeit('for i in l: _ = i', globals=globals(), number=1000),
    'deque single_out': timeit('for i in d: _ = i', globals=globals(), number=1000)
}

for k, v in results_3.items(): print(f'{k}: {v}')

# list append: 0.004946416000000002
# deque append: 0.004542542
# list extend: 0.0002581670000000001
# deque extend: 0.0005144579999999989
# list pop: 3.945800000000263e-05
# deque pop: 4.1290999999998856e-05
# ----------------------------------------------------------------------------------------------------
# list insert: 12.525800834
# deque appendleft: 0.003626249999999942
# list pop: 4.049660874999999
# deque popleft: 0.00335741700000014
# list extend left: 0.03991445899999846
# deque extendleft: 0.00040566700000255196
# ----------------------------------------------------------------------------------------------------
# list single_out: 1.8636680000000005
# deque single_out: 1.973922292000001

# в операциях/методах, предназначенных для списков, списки преимущественно быстрее,
# похожая ситуация и для операций, созданных для деков. как и ожидалось,
# согласно пройденным материалам
