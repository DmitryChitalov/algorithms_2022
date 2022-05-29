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
from random import random


# 1
def app_list(user_list, num=1000):
    for i in range(num):
        user_list.append(i)
    return user_list


def pop_list(user_list, num=1000):
    for i in range(num):
        user_list.pop()
    return user_list


def ext_list(user_list, num=1000):
    for i in range(num):
        user_list.extend([i])
    return user_list


# 2
def l_app_list(user_list, num=1000):
    for i in range(num):
        user_list.appendleft(i)
    return user_list


def ul_app_list(user_list, num=1000):
    for i in range(num):
        user_list.insert(0, i)
    return user_list


def l_pop_list(user_list, num=1000):
    for i in range(num):
        user_list.popleft()
    return user_list


def ul_pop_list(user_list, num=1000):
    for i in range(num):
        user_list.pop(0)
    return user_list


def l_ext_list(user_list, num=1000):
    for i in range(num):
        user_list.extendleft([i, '0'])
    return user_list


def ul_ext_list(user_list, num=1000):
    for i in range(num):
        el = [i, '0']
        user_list = el + user_list
    return user_list


# 3

def u_take_el(user_list, num=1000):
    for i in range(num):
        el = round(random() * 1000)
        answ_el = user_list[el]


def d_take_el(user_list, num=1000):
    for i in range(num):
        el = round(random() * 1000)
        answ_el = user_list[el]



# 1 append, pop, extend
my_u_list = list('abcdef')
my_list = list('abcdef')
my_list = deque(my_list)
u_test = app_list(my_u_list)
d_test = app_list(my_list)

print('append ', timeit('u_test', globals=globals(), number=10000))
print('append deque ', timeit('d_test', globals=globals(), number=10000))

u_test_pop = pop_list(my_u_list)
d_test_pop = pop_list(my_list)

print('pop ', timeit('u_test_pop', globals=globals(), number=10000))
print('pop deque ', timeit('d_test_pop', globals=globals(), number=10000))

u_test_ext = ext_list(my_u_list)
d_test_ext = ext_list(my_list)

print('extend ', timeit('u_test_ext', globals=globals(), number=10000))
print('extend deque ', timeit('d_test_ext', globals=globals(), number=10000))

# Использование deque для append, pop, extend незначительно замедляет код

# appendleft, popleft, extendleft
u_left_app = ul_app_list(my_u_list)
d_left_app = l_app_list(my_list)
print('appendleft', timeit('u_left_app', globals=globals(), number=10000))
print('appendleft deque ', timeit('d_left_app', globals=globals(), number=10000))

u_left_pop = ul_pop_list(my_u_list)
d_left_pop = l_pop_list(my_list)
print('popleft ', timeit('u_left_pop', globals=globals(), number=10000))
print('popleft deque ', timeit('d_left_pop', globals=globals(), number=10000))

u_left_ext = ul_ext_list(my_u_list)
d_left_ext = l_ext_list(my_list)
print('extendleft ', timeit('u_left_ext', globals=globals(), number=10000))
print('extendleft deque ', timeit('d_left_ext', globals=globals(), number=10000))

# Использование appendleft, popleft, extendleft дека ускоряет код и делает код читабельнее

# 3
u_new_list = u_take_el(my_u_list)
d_new_list = d_take_el(my_list)
print('take el ', timeit('u_new_list', globals=globals(), number=10000))
print('take el deque ', timeit('d_new_list', globals=globals(), number=10000))

# При получении элемента деком скорость не увеличилась.