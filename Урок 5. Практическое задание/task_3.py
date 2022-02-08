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
from random import randint
from timeit import timeit


def append_n(collection, n=100):
    """
    Универсальная функция для вставки. В реализации никаких различий нет.
    """
    for i in range(0, n):
        collection.append(i)


def pop_all(input_lst):
    """
    Универсальная функция для удаления последнего элемента. В реализации никаких различий нет.
    """
    for _ in range(0, len(input_lst)):
        input_lst.pop()


def extend_n(collection, n=100):
    """
    Универсальная функция для расширения массива. В реализации никаких различий нет.
    """
    for _ in range(0, n):
        collection.extend([0, 1, 2])


def appendleft_n(deq, n=100):
    """
    Функция для вставки слева в deque.
    """
    for i in range(0, n):
        deq.appendleft(i)


def appendleft_n_lst(lst, n=100):
    """
    Функция для вставки слева в list. Отдельного метода для вставки слева у списка нет,
    поэтому используем обычный insert.
    """
    for i in range(0, n):
        lst.insert(0, i)


def popleft_n(deq):
    """
    Функция для удаления слева в deque.
    """
    for i in range(0, len(deq)):
        deq.popleft()


def popleft_n_lst(lst):
    """
    Функция для удаления слева в list. Отдельного метода для удаления слева у списка нет,
    поэтому используем обычный pop с параметром 0.
    """
    for i in range(0, len(lst)):
        lst.pop(0)


def extend_left_n(deq, n=100):
    """
    Функция для расщирения слева в deque.
    """
    for _ in range(0, n):
        deq.extendleft([0, 1, 2])


def extend_left_n_lst(lst, n=100):
    """
    Функция для расщирения слева в list. Отдельного метода для расщирения слева у списка нет,
    поэтому используем обычный pop с параметром 0.
    """
    for _ in range(0, n):
        lst.insert(0, [0, 1, 2])


def get_random_element(collection):
    return collection[randint(0, len(collection) - 1)]


lst = []
deq = deque()
num = 1000

print('******* Операции append\n')
print('Append в list: ')
print(
    timeit(
        'append_n(lst)',
        globals=globals(),
        number=num
    )
)
print('Append в deque: ')
print(
    timeit(
        'append_n(deq)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции pop \n')
print('Pop из list: ')
print(
    timeit(
        'pop_all(lst)',
        globals=globals(),
        number=num
    )
)
print('Pop из deque: ')
print(
    timeit(
        'pop_all(deq)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции extend \n')
print('Extend в list: ')
print(
    timeit(
        'extend_n(lst, n = 10)',
        globals=globals(),
        number=num
    )
)
print('Extend в deque: ')
print(
    timeit(
        'extend_n(deq, n = 10)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции appendleft \n')
print('Appendleft в list: ')
print(
    timeit(
        'appendleft_n_lst(lst)',
        globals=globals(),
        number=num
    )
)
print('Appendleft в deque: ')
print(
    timeit(
        'appendleft_n(deq)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции popleft \n')
print('Popleft из list: ')
print(
    timeit(
        'popleft_n_lst(lst)',
        globals=globals(),
        number=num
    )
)
print('Popleft из deq: ')
print(
    timeit(
        'popleft_n(deq)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции extendleft  \n')
print('extendleft из lst: ')
print(
    timeit(
        'extend_left_n_lst(lst)',
        globals=globals(),
        number=num
    )
)
print('extendleft из deq: ')
print(
    timeit(
        'extend_left_n(deq)',
        globals=globals(),
        number=num
    )
)


print('\n******* Операции взятия элементов  \n')
print('Из списка: ')
print(
    timeit(
        'get_random_element(lst)',
        globals=globals(),
        number=num
    )
)
print('Из deq: ')
print(
    timeit(
        'get_random_element(deq)',
        globals=globals(),
        number=num
    )
)
