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

"""


from timeit import timeit
from collections import deque
tlist = []
tdeque = deque()


def list_app(list):
    for x in range(10**5):
        list.append(x)


print('list.append : \n', timeit('list_app(tlist)', globals=globals(), number=100))


def deq_app(dq_obj):
    for x in range(10**5):
        dq_obj.append(x)


print('deque.append : \n', timeit('deq_app(tdeque)', globals=globals(), number=100))


def list_pop(list):
    for x in range(10**5):
        list.pop()


print('list.pop : \n', timeit('list_pop(tlist)', globals=globals(), number=100))


def deq_pop(dq_obj):
    for x in range(10**5):
        dq_obj.pop()


print('deque.pop : \n', timeit('deq_pop(tdeque)', globals=globals(), number=100))


def list_ext(list):
    for x in range(10**5):
        list.extend([1, 2, 3, 4, 5])


print('list.extend : \n', timeit('list_ext(tlist)', globals=globals(), number=100))


def deq_ext(dq_obj):
    for x in range(10**5):
        dq_obj.extend([1, 2, 3, 4, 5])


print('deque.extend : \n', timeit('deq_ext(tdeque)', globals=globals(), number=100))


"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""

def list_appleft(list):
    for x in range(10):
        list.insert(0, x)


print('list.appendleft : \n', timeit('list_appleft(tlist)', globals=globals(), number=10))


def deq_appleft(dq_obj):
    for x in range(10**5):
        dq_obj.appendleft(x)


print('deque.appendleft : \n', timeit('deq_appleft(tdeque)', globals=globals(), number=100))


def list_popleft(list):
    for x in range(10):
        list.pop(0)


print('list.popleft : \n', timeit('list_popleft(tlist)', globals=globals(), number=10))


def deq_popleft(dq_obj):
    for x in range(10**5):
        dq_obj.popleft()


print('deque.popleft : \n', timeit('deq_popleft(tdeque)', globals=globals(), number=100))


def list_extendleft(list):
    for x in range(10):
        list.extend([1, 2, 3, 4, 5])
        list.sort()


print('list.extendleft : \n', timeit('list_extendleft(tlist)', globals=globals(), number=10))


def deq_extendleft(dq_obj):
    for x in range(10**5):
        dq_obj.extendleft([1, 2, 3, 4, 5])


print('deque.extendleft : \n', timeit('deq_extendleft(tdeque)', globals=globals(), number=100))

"""
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

def list_get(list):
    for x in range(10**5):
        z = list[x]


print('list.get : \n', timeit('list_get(tlist)', globals=globals(), number=100))


def deq_get(dq_obj):
    for x in range(10**5):
        z = list[dq_obj]


print('deque.get : \n', timeit('deq_get(tdeque)', globals=globals(), number=100))


"""
1) Операции append, pop, extend списка и дека занимают примерно одно и то же время
2) Операции appendleft, popleft, extendleft выполняются гораздо быстрее в Деке
3) Операции получения элемента списка выполняются заметно быстрее, чем те же операции в Деке
"""