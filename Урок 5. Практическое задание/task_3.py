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

from timeit import timeit
from collections import deque

#  1) сравнить операции

n = 100
my_list = []
list_deque = deque()
list_test = [i for i in range(100)]


def list_append(num):
    for i in range(n):
        my_list.append(i)


def deque_append(num):
    for i in range(n):
        list_deque.append(i)


def pop_list(num):
    for i in range(len(my_list)):
        my_list.pop()


def pop_deque(num):
    for i in range(len(deque())):
        list_deque.pop()


def extend_list(num):
    for i in range(n):
        my_list.extend(list_test)


def extend_deque(num):
    for i in range(n):
        list_deque.extend(list_test)


print(f'Время выполнения функции list_append = {timeit("list_append(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции deque_append = {timeit("deque_append(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции pop_list = {timeit("pop_list(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции pop_deque = {timeit("pop_deque(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции extend_list = {timeit("extend_list(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции extend_deque = {timeit("extend_deque(n)", globals=globals(), number=100)}')

"""
Выводы:
Время выполнения функции list_append = 0.00046980002662166953
Время выполнения функции deque_append = 0.0008847999852150679
Время выполнения функции pop_list = 0.0004953999887220562
Время выполнения функции pop_deque = 2.239999594166875e-05
Время выполнения функции extend_list = 0.01565740001387894
Время выполнения функции extend_deque = 0.00469959998736158

append в list быстрее
pop в list быстрее
extend в deque быстрее
"""

pop_list(n)
pop_deque(n)

#  2) сравнить операции


def list_append_left(num):
    for i in range(n):
        my_list.insert(0, i)


def deque_append_left(num):
    for i in range(n):
        list_deque.appendleft(i)


def pop_left_list(num):
    for i in range(len(my_list)):
        my_list.pop(0)


def pop_left_deque(num):
    for i in range(len(deque())):
        list_deque.popleft()


def extend_left_list(num):
    for i in range(n):
        my_list.insert(0, list_test)


def extend_left_deque(num):
    for i in range(n):
        list_deque.extendleft(list_test)


print(f'Время выполнения функции list_append_left = {timeit("list_append_left(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции deque_append_left = {timeit("deque_append_left(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции pop_left_list = {timeit("pop_left_list(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции pop_left_deque = {timeit("pop_left_deque(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции extend_left_list = {timeit("extend_left_list(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции extend_left_deque = {timeit("extend_left_deque(n)", globals=globals(), number=100)}')


"""
Выводы:
Время выполнения функции lst_append_left = 0.01262459997087717
Время выполнения функции deque_append_left = 0.00045680004404857755
Время выполнения функции pop_left_lst = 0.0062070999993011355
Время выполнения функции pop_left_deque = 2.2799998987466097e-05
Время выполнения функции extend_left_lst = 0.012461500009521842
Время выполнения функции extend_left_deque = 0.006367699999827892

appendleft, extendleft в deque быстрее соответствующих им операций списка
popleft медленнее, хотя судя по уроку и их константной сложности должны все быть быстрее
"""

# 3) сравнить операции получения элемента списка и дека


def get_list(num):
    for i in range(n):
        my_list[i] = i


def get_list_deque(num):
    for i in range(n):
        list_deque[i] = i


print(f'Время выполнения функции get_list = {timeit("get_list(n)", globals=globals(), number=100)}')
print(f'Время выполнения функции get_list_deque = {timeit("get_list_deque(n)", globals=globals(), number=100)}')

"""
Выводы
Время выполнения функции get_list = 0.0002733999863266945
Время выполнения функции get_list_deque = 0.00047610001638531685

Обычный список работает быстрее
"""
