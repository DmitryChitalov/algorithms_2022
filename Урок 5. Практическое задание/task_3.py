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

N = 10000
NUMBER = 100
ADDITION_LIST = list(range(NUMBER))


def _append(obj):
    for i in range(N):
        obj.append(i)


def _pop(obj):
    for _ in range(N):
        obj.pop()


def _extend(obj):
    for _ in range(100):
        obj.extend(ADDITION_LIST)  # 100 x 100 = 10_000


def _appendleft(obj):
    for i in range(N):
        if type(obj) == list:
            obj.insert(0, i)
        else:
            obj.appendleft(i)


def _popleft(obj):
    for i in range(N):
        if type(obj) == list:
            obj.pop(0)
        else:
            obj.popleft()


def _extendleft_list():
    global LIST
    for i in range(100):
        LIST = LIST[::-1]
        LIST.extend(ADDITION_LIST)
        LIST = LIST[::-1]


def _extendleft(obj):
    for i in range(100):
        obj.extendleft(ADDITION_LIST)


def get_elem(obj):
    for i in range(N):
        x = obj[i]


if __name__ == '__main__':
    LIST = list()
    DEQUE = deque()
    print('append list:', timeit('_append(LIST)', globals=globals(), number=NUMBER))
    print('append deque:', timeit('_append(DEQUE)', globals=globals(), number=NUMBER))
    print('pop list:', timeit('_pop(LIST)', globals=globals(), number=NUMBER))
    print('pop deque:', timeit('_pop(DEQUE)', globals=globals(), number=NUMBER))
    print('extend list:', timeit('_extend(LIST)', globals=globals(), number=NUMBER))
    print('extend deque:', timeit('_extend(DEQUE)', globals=globals(), number=NUMBER))
    print('_' * 150)
    LIST = list()
    DEQUE = deque()
    print('insert list:', timeit('_appendleft(LIST)', globals=globals(), number=3))
    print('appendleft deque:', timeit('_appendleft(DEQUE)', globals=globals(), number=NUMBER))
    # print(len(LIST), len(DEQUE))
    LIST = list(range(1_000_000))
    print('pop(0) list:', timeit('_popleft(LIST)', globals=globals(), number=3))
    print('popleft deque:', timeit('_popleft(DEQUE)', globals=globals(), number=NUMBER))
    # print(len(LIST), len(DEQUE))
    LIST = list()
    print('extendleft list:', timeit('_extendleft_list()', globals=globals(), number=3))
    print('extendleft deque:', timeit('_extendleft(DEQUE)', globals=globals(), number=NUMBER))
    # print(len(LIST), len(DEQUE))
    print('_' * 150)
    LIST = list(range(1_000_000))
    print('get elem list:', timeit('get_elem(LIST)', globals=globals(), number=NUMBER))
    print('get elem deque:', timeit('get_elem(DEQUE)', globals=globals(), number=NUMBER))

    """
    1) Append, pop, extend:
        - Append в список выполняется медленней, чем в деку
            append list: 0.11780495799939672
            append deque: 0.08044332100143947
        - Pop из списка выполняется медленней, чем из деки
            pop list: 0.0885841489998711
            pop deque: 0.0696852540004329
        - Extend в список выполняется быстрей, чем в деку
            extend list: 0.005087224000817514
            extend deque: 0.0060997719992883
    2) Appendleft, popleft, extendleft
        - Insert в 0 у списка выполняется намного дольше, чем у деки
            insert list: 0.2695857150010852 (3 запуска, 30_000 элементов)
            appendleft deque: 0.1784589210001286 (100 запусков, 1_000_000 элементов)
        - Pop из 0 у списка выполняется также намного дольше, чем у деки
            pop(0) list: 27.66640114599977 (3 запуска, 30_000 элементов)
            popleft deque: 0.18639843900018604 (100 запусков, 1_000_000 элементов)
        - Extendleft у списка нет. Костылями выполняется дольше, чем у деки
            extendleft list: 0.023574799999551033 (3 запуска, 30_000 элементов)
            extendleft deque: 0.006385316999512725 (100 запусков, 1_000_000 элементов)
    3) Получение элементов по списку
        - По индексу получение элементов выполняется быстрей у списка
            get elem list: 0.051357715999984066
            get elem deque: 0.19932398700075282
    """