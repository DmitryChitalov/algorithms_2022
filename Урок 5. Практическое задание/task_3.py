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
from timeit import timeit
from random import randrange
from collections import deque

my_list = []
my_deque = deque()


def list_fill():
    my_list.clear()
    for i in range(size):
        my_list.append(randrange(100))


def deque_fill():
    my_deque.clear()
    for i in range(size):
        my_deque.append(randrange(100))


def list_app():
    for i in range(n):
        my_list.append(1)


def deque_app():
    for i in range(n):
        my_deque.append(1)


def list_pop():
    for i in range(n):
        my_list.pop()


def deque_pop():
    for i in range(n):
        my_deque.pop()


def list_extend():
    for i in range(n):
        my_list.extend([2, 2])


def deque_extend():
    for i in range(n):
        my_deque.extend([2, 2])


def list_app_2():
    for i in range(n):
        my_list.insert(0, 1)


def deque_appleft():
    for i in range(n):
        my_deque.appendleft(1)


def list_pop_2():
    for i in range(n):
        my_list.remove(my_list[0])


def deque_popleft():
    for i in range(n):
        my_deque.popleft()


def list_extend_2():
    for i in range(n):
        for item in [2, 2]:
            my_list.insert(0, item)


def deque_extleft():
    for i in range(n):
        my_deque.extendleft([2, 2])


def list_get():
    for i in range(n):
        item = my_list[index]


def deque_get():
    for i in range(n):
        for j in range(index + 1):
            item = my_deque.popleft()


size = 100
list_fill()
deque_fill()
print('Операции в конце:')
n = 100
for func_name in (
    'list_app()', 'deque_app()'
    , 'list_pop()', 'deque_pop()'
    , 'list_extend()', 'deque_extend()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=100000)}')

print('Операции в начале:')
n = 100
for func_name in (
    'list_app_2()', 'deque_appleft()'
    , 'list_pop_2()', 'deque_popleft()'
    , 'list_extend_2()', 'deque_extleft()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=1)}')

print('Операции извлечения:')
size = 1000000
list_fill()
deque_fill()
n = 300
index = 100
for func_name in (
    'list_get()', 'deque_get()'
):
    print(f'{func_name}: время = {timeit(func_name, globals=globals(), number=1)}')

'''
Скорость выполнения операций в конце для списка и дека - почти одинаковая.
Скорость выполнения операций в начале списка - на порядки ниже скорости для дека. 
Зависит от размера списка.
Скорость извлечения элемента из списка - на порядки выше скорости для дека. 
Зависит от размера дека.
'''
