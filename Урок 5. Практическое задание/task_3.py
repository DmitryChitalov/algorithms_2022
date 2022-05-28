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
########################################################################
from collections import deque
from timeit import timeit

my_list = list()
my_dq = deque()
my_num = 10 ** 3
my_num2 = 10 ** 2


# 1) сравниваем операции append, pop, extend:

def create_array(lst, n):
    for i in range(n):
        lst.append(i)


def pop_array(lst, n):
    for i in range(n):
        lst.pop()


def extend_array(lst, n):
    for i in range(n):
        lst.extend([i + 1])


# 2) сравниваем операции appendleft, popleft, extendleft:

def ins_lst(lst, n):
    for i in range(n):
        lst.insert(0, i)


def app_left_dq(dq, n):
    for i in range(n):
        dq.appendleft(i)


def pop_lst(lst, n):
    for i in range(n):
        lst.pop(0)


def pop_left_dq(dq, n):
    for i in range(n):
        dq.popleft()


def ext_left_lst(lst, n):
    for i in range(n):
        lst[:0] = [i]


def ext_left_dq(dq, n):
    my_str = str('')
    for i in range(n):
        my_str += str(i)
        dq.extendleft(my_str)


# 3) сравниваем операции получения элемента списка и дека:

def get_lst(lst, n):
    for i in range(n):
        lst[i] = i
    return lst


def get_dq(dq, n):
    for i in range(n):
        dq[i] = i
    return dq


print('append, pop, extend:')
print('my_list: ', timeit("create_array(my_list, my_num)", globals=globals(), number=10000))
print('my_dq: ', timeit("create_array(my_dq, my_num)", globals=globals(), number=10000))
print()
print('my_list: ', timeit("pop_array(my_list, my_num)", globals=globals(), number=10000))
print('my_dq: ', timeit("pop_array(my_dq, my_num)", globals=globals(), number=10000))
print()
print('my_list: ', timeit("extend_array(my_list, my_num)", globals=globals(), number=10000))
print('my_dq: ', timeit("extend_array(my_dq, my_num)", globals=globals(), number=10000))
print()

print('appendleft, popleft, extendleft:')
print('my_list: ', timeit("ins_lst(my_list, my_num2)", globals=globals(), number=10))
print('my_dq: ', timeit("app_left_dq(my_dq, my_num2)", globals=globals(), number=10))
print()
print('my_list: ', timeit("pop_lst(my_list, my_num2)", globals=globals(), number=10))
print('my_dq: ', timeit("pop_left_dq(my_dq, my_num2)", globals=globals(), number=10))
print()
print('my_list: ', timeit("ext_left_lst(my_list, my_num2)", globals=globals(), number=10))
print('my_dq: ', timeit("ext_left_dq(my_dq, my_num2)", globals=globals(), number=10))
print()
print('get:')
print('my_list: ', timeit("get_lst(my_list, my_num)", globals=globals(), number=10000))
print('my_dq: ', timeit("get_dq(my_dq, my_num)", globals=globals(), number=10000))
print()

"""
Вывод:
1) сравнивая операции append, pop, extend списка и дека можно
прийти к выводу, что дек опережает список при выполнении 
операции append. При операциях pop, extend у них паритет.
2) сравнивая операции appendleft, popleft, extendleft списка и дека можно
прийти к выводу, что дек опережает список при выполнении 
этих операции. Особенно при выполнении  операции extendleft.
3) сравнивая операции получения элемента списка и дека 
видно, что список опережает дек.
Что доказывает основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
"""
