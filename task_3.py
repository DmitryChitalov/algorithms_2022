"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
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
(append, pop и т.д.) проводить в циклах
"""
from collections import deque
from timeit import timeit

# lst_test = [5, 60, 900]
# deq_test = deque('307981456820')
lst_test = [i for i in range(10 ** 5)]
deq_test = deque([i for i in range(10 ** 5)])


num = 50

""" 1. append, pop, extend списка и дека """
# Список


def append_to_lst(lst_test):
    for i in range(num):
        lst_test.append(i)
    return lst_test


def pop_from_lst(lst_test):
    for i in range(num):
        lst_test.pop()
    return lst_test


def extend_lst(lst_test):
    for i in range(num):
        lst_test.extend([1, 9])
    return lst_test

# Дек


def append_to_deq(deq_test):
    for i in range(num):
        deq_test.append(i)
    return deq_test


def pop_from_deq(deq_test):
    for i in range(num):
        deq_test.pop()
    return deq_test


def extend_deq(deq_test):
    for i in range(num):
        deq_test.extend([1, 9])
    return deq_test


# Замеры времени
print(timeit("append_to_lst(lst_test)", globals=globals()))
print(timeit("append_to_deq(deq_test)", globals=globals()))
print(timeit("pop_from_lst(lst_test)", globals=globals()))
print(timeit("pop_from_deq(deq_test)", globals=globals()))
print(timeit("extend_lst(lst_test)", globals=globals()))
print(timeit("extend_deq(deq_test)", globals=globals()))

"""
7.5607793999999995
6.2132991

6.8419484000000015
5.5288017000000025

13.0597003
14.391736799999997

Операции добавления элементов в конец списка и дека, удаление элементов, операции по вставке списка в конец списка, дека
производятся за равные промежутки времени (но мой ноутбук считает иначе :) , цифры немного отличаются)
"""
