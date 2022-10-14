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

test_lst = [i for i in range(1, 50)]
my_lst = [i for i in range(1, 1000)]
test_dq = deque(i for i in range(1, 1000))


print('-------------------deque.append vs list.append')
print(timeit('for i in range(100): test_dq.append(i)', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.append(i)', globals=globals(), number=5000))
print('-----------------deque.pop vs list.pop')
print(timeit('for i in range(100): test_dq.pop()', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.pop()', globals=globals(), number=5000))
print('-------------------deque.extend vs list.extend')
print(timeit('for i in range(100): test_dq.extend(my_lst)', globals=globals(), number=5000))
print(timeit('for i in range(100): test_lst.extend(my_lst)', globals=globals(), number=5000))
"""
append, pop, extend быстрее в deque. Вероятно связано с тем, что сложность deque - O(1),
а списка - O(n)

"""


print('------------------deque.appendleft vs list.insert(0...)')
print(timeit('for i in range(5): test_dq.appendleft(i)', globals=globals(), number=10))
print(timeit('for i in range(5): test_lst.insert(0, i)', globals=globals(), number=10))
print('------------------deque.extendleft vs list."конкатенация"')
print(timeit('test_dq.extendleft(my_lst)', globals=globals(), number=10))
print(timeit('my_lst + test_lst', globals=globals(), number=10))
print('-----------------deque.popleft vs list.pop(0)')
print(timeit('for i in range(10): test_dq.popleft()', globals=globals(), number=10))
print(timeit('for i in range(10): my_lst.pop()', globals=globals(), number=10))
"""
appendleft, extendleft - deque быстрее
popleft - список быстрее
"""


print('--------------Получение элементов по индексу (deque[..] vs list[..])')
print(timeit('for i in range(100): test_dq[i]', globals=globals(), number=10000))
print(timeit('for i in range(100): test_lst[i]', globals=globals(), number=10000))
"""
  deque быстрее при большой выборке
"""
