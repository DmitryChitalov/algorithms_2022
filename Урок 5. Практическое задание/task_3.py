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

some_lst = [i for i in range(10000)]
some_deque = deque([i for i in range(10000)])
n = 1000


def append_list(some_lst):
    for i in range(n):
        some_lst.append(i)
    return some_lst


def append_deque(some_deque):
    for i in range(n):
        some_deque.append(i)
    return some_deque


def pop_list(some_lst):
    for i in range(n):
        some_lst.pop()
    return some_lst


def pop_deque(some_deque):
    for i in range(n):
        some_deque.pop()
    return some_deque


def extend_list(some_lst):
    for i in range(n):
        some_lst.extend([1, 2, 3])
    return some_lst


def extend_deque(some_deque):
    for i in range(n):
        some_deque.extend([1, 2, 3])
    return some_deque


def appendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, i)
    return some_lst


def appendleft_deque(some_deque):
    for i in range(n):
        some_deque.appendleft(i)
    return some_deque


def popleft_list(some_lst):
    for i in range(n):
        some_lst.pop(i)
    return some_lst


def popleft_deque(some_deque):
    for i in range(n):
        some_deque.popleft()
    return some_deque


def extendleft_list(some_lst):
    for i in range(n):
        some_lst.insert(0, [1, 2, 3])
    return some_lst


def extendleft_deque(some_deque):
    for i in range(n):
        some_deque.extendleft([1, 2, 3])
    return some_deque


def get_elem_list(some_lst):
    for i in range(n):
        some_lst[i] = i
    return some_lst


def get_elem_deque(some_deque):
    for i in range(n):
        some_deque[i] = i
    return some_deque


def analize():
    print(f'Анализируем:\n'
          f'результат: list/deque (sec)')
    print(f"append: "
        f"{(timeit('append_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('append_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"extend: "
        f"{(timeit('extend_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('extend_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"pop: "
        f"{(timeit('pop_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('pop_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"appendleft: "
        f"{(timeit('appendleft_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('appendleft_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"extendleft: "
        f"{(timeit('extendleft_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('extendleft_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"popleft: "
        f"{(timeit('popleft_list(some_lst.copy())', globals=globals(), number=100))}/"
        f"{(timeit('popleft_deque(some_deque.copy())', globals=globals(), number=100))}")
    print(f"get element: "
          f"{(timeit('get_elem_list(some_lst.copy())', globals=globals(), number=100))}/"
          f"{(timeit('get_elem_deque(some_deque.copy())', globals=globals(), number=100))}")

analize()

"""
Специфические методы deque работающие с началом списка значительно быстрее чем 
аналоги в list.  Остальные тесты показывают преимущество при работе с list

"""