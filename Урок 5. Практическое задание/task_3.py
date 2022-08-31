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
from random import randrange

my_deque = deque()
my_list = list()

tests_number = 100000

print('.append')
print('deque', end=' ')
print(timeit('my_deque.append(randrange(0,tests_number))', globals=globals()))
print('list', end=' ')
print(timeit('my_list.append(randrange(0,tests_number))', globals=globals()))

print('.pop')
print('deque', end=' ')
print(timeit('my_deque.pop()', globals=globals()))
print('list', end=' ')
print(timeit('my_list.pop()', globals=globals()))

print('.extend')
print('deque', end=' ')
print(timeit('my_deque.extend([i for i in range(1, 5)])', globals=globals(), number=tests_number))
print('list', end=' ')
print(timeit('my_list.extend([i for i in range(1, 5)])', globals=globals(), number=tests_number))

'''
Выводы. Эти операции выполняются с помощью дека немного медленнее, чем с помощью списка.
'''

print('.appendleft / .insert(0)')
print('deque', end=' ')
print(timeit('my_deque.appendleft(5)', globals=globals(), number=tests_number))
print('list', end=' ')
print(timeit('my_list.insert(0, 5)', globals=globals(), number=tests_number))

print('.popleft / .pop(0)')
print('deque', end=' ')
print(timeit('my_deque.popleft()', globals=globals(), number=tests_number))
print('list', end=' ')
print(timeit('my_list.pop(0)', globals=globals(), number=tests_number))

print('.extendleft')
print('deque', end=' ')
print(timeit('my_deque.extendleft([i for i in range(1, 5)])', globals=globals(), number=tests_number))
print('list', end=' ')
print(timeit('my_list[:0] = [i for i in range(1, 5)]', globals=globals(), number=tests_number))

'''
Выводы. Эти операции выполняются с помощью дека намного быстрее, чем с помощью списка.
'''

print('Получение элемента')
print('deque', end=' ')
print(timeit('my_deque[randrange(0, len(my_deque))]', globals=globals(), number=tests_number))
print('list', end=' ')
print(timeit('my_list[randrange(0, len(my_list))]', globals=globals(), number=tests_number))

'''
Выводы. Получение элемента из дека происходит в несколько раз медленнее, чем из списка.
'''

