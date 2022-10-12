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

import timeit
from collections import deque

# 1
l = list('задача')
d = deque('задача')
print("1. append для list:", timeit.timeit('l.append("_")', number=10000, globals=globals()))
print("1. append для deque:", timeit.timeit('d.append("_")', number=10000, globals=globals()))
print('1. append: Время list практически равно deque')
print("1. pop для list:", timeit.timeit('l.pop()', number=10000, globals=globals()))
print("1. pop для deque:", timeit.timeit('d.pop()', number=10000, globals=globals()))
print('1. pop: Время list чуть меньше deque')
print("1. extend для list:", timeit.timeit('l.extend("_3")', number=10000, globals=globals()))
print("1. extend для deque:", timeit.timeit('d.extend("_3")', number=10000, globals=globals()))
print('1. extend: Время list кратно больше deque')
"""
Там где работа с list и deque ведется в конце (добавление в конец, удаление из конца) время незначительно отличается.
Но при расширении list и deque видна скорость deque, т.к. к list по сути добавляется новый list, 
и там (во втором list) происходит смещение порядка элементов, на что тратится больше времени нежели в deque.
"""

# 2
l = list('задача')
d = deque('задача')
print("2. appendleft для list:", timeit.timeit('l.insert(0, "_")', number=10000, globals=globals()))
print("2. appendleft для deque:", timeit.timeit('d.appendleft("_")', number=10000, globals=globals()))
print('2. appendleft: Время list кратно больше deque')
print("2. popleft для list:", timeit.timeit('l.pop(0)', number=10000, globals=globals()))
print("2. popleft для deque:", timeit.timeit('d.popleft()', number=10000, globals=globals()))
print('2. popleft: Время list кратно больше deque')
print("2. extendleft для list:", timeit.timeit('l[:0]="2_"', number=10000, globals=globals()))
print("2. extendleft для deque:", timeit.timeit('d.extendleft("_2")', number=10000, globals=globals()))
print('2. extendleft: Время list кратно больше deque')
"""
При изменении в начале list и deque видно преимущество deque. Т.к. все эти действия влияют на смещение 
порядка элементов в list, на что тратится больше времени нежели в dequeе
"""

# 3
l = list('задача')
d = deque('задача')
print("3. Взять элемент в list:", timeit.timeit('l[2]', number=10000, globals=globals()))
print("3. Взять элемент в deque:", timeit.timeit('d[2]', number=10000, globals=globals()))
print('3. Взять элемент: Время list немного меньше deque')
"""
Получение элемента в list и deque практически одинаково, лишь с небольшой разницей в пользу list.
При этом не принципиальной разницей, и можно сказать время получения элементов в list и deque одинаково.
"""