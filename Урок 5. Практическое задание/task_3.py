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

# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dq = deque(lst)

# append
print('append:')
print(timeit('for i in range(100):' 
             '  dq.append(1)', globals=globals(), number=100000))
print(timeit('for i in range(100):' 
             '  lst.append(1)', globals=globals(), number=100000))

# pop
print('pop:')
print(timeit('for i in range(100):' 
             '  dq.pop()', globals=globals(), number=100000))
print(timeit('for i in range(100):' 
             '  lst.pop()', globals=globals(), number=100000))

# extend
print('extend:')
print(timeit('for i in range(100):' 
             '  dq.extend([0, 0, 0])', globals=globals(), number=100000))
print(timeit('for i in range(100):' 
             '  lst.extend([0, 0, 0])', globals=globals(), number=100000))

del dq

"""
append:
    0.6383225999306887
    0.7939871998969465
pop:
    0.5577096999622881
    0.5859202998690307
extend:
    1.4741106000728905
    1.6710582999512553

Все эти операции для дека выполняются чуть быстрее. Хотя в очень редких случаях в методе pop список бывает ооочень 
немножко быстрее 
"""

# 2) сравнить операции
# appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dq = deque(lst)

# appendleft и insert(0,)
print('appendleft и insert(0,):')
print(timeit('for i in range(100):' 
             '  dq.appendleft(0)', globals=globals(), number=1000))
print(timeit('for i in range(100):' 
             '  lst.insert(0, 0)', globals=globals(), number=1000))

# popleft и pop(0)
print('popleft и pop(0):')
print(timeit('for i in range(100):' 
             '  dq.popleft()', globals=globals(), number=1000))
print(timeit('for i in range(100):' 
             '  lst.pop(0)', globals=globals(), number=1000))

# appendleft и +
print('extendleft и +:')
print(timeit('for i in range(100):' 
             '  dq.extendleft([0,0,0])', globals=globals(), number=1000))
print(timeit('for i in range(100):' 
             '  [0,0,0] + lst', globals=globals(), number=1000))

del dq

"""
appendleft и insert(0,):
    0.006131999893113971
    2.0839732999447733
popleft и pop(0):
    0.005553700029850006
    1.0657677999697626
extendleft и +:
    0.014398799976333976
    0.011945200152695179

Во всех операциях кроме extendleft дек оказался намного быстрее
"""

# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dq = deque(lst)

# [x]
print('[x]:')
print(timeit('for i in range(100):' 
             '  dq[4]', globals=globals(), number=1000000))
print(timeit('for i in range(100):' 
             '  lst[4]', globals=globals(), number=1000000))

"""
[x]:
    4.370097300037742
    3.8018153000157326

Обращение к произвольному элементу списка быстрее 
"""