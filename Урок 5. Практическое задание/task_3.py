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

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit
from random import randint

n = 10 ** 4
some_lst1 = []
some_deque1 = deque()
some_lst2 = [i for i in range(10 ** 5)]
some_deque2 = deque([i for i in range(10 ** 5)])


def fill_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst


def fill_deque(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq


def change_list(lst):
    for _ in range(90000):
        lst[randint(1, 8001)] = randint(1, 150)
    return lst


def change_deque(dq):
    for _ in range(90000):
        dq[randint(1, 8001)] = randint(1, 150)
    return dq


if __name__ == '__main__':
    print('Время заполнения списка при 10 повторениях: ', timeit(
        'fill_list(some_lst1)',
        setup='from __main__ import fill_list, some_lst1, n',
        number=10
    ))

    print('Время заполнения двусторонней очереди при 10 повторениях: ', timeit(
        'fill_deque(some_deque1)',
        setup='from __main__ import fill_deque, some_deque1, n',
        number=10
    ))
    """
    Если заполнение списка проиходит путем вставки элемента в начало списка, 
    то двусторонняя очередь работает гораздо
    быстрее, чем обычный список, так как сложность операции вставки в начало 
    и конец для нее О(1), для списка же
    сложность операции вставки в начало - О(n).
    Если заполнять списки путем добавления элементов в конец списка, 
    то время работы сопоставимо, так как сложность
    операции составляет О(1) и в том и другом случае. Дек заполняется 
    чуть быстрее при большом количестве элементов.
    """

    print('-' * 50)
    print('Время изменения списка при 10 повторениях: ', timeit(
        'change_list(some_lst2)',
        setup='from __main__ import change_list, some_lst2',
        number=10
    ))
    print('Время изменения двусторонней очереди при 10 повторениях: ', timeit(
        'change_deque(some_deque2)',
        setup='from __main__ import change_deque, some_deque2',
        number=10
    ))
    """
    При случайном доступе к элементу по индексу и изменении элемента,
    обычный список работает быстрее, чем дек.
    """

