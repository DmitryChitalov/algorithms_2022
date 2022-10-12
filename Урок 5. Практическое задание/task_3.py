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

append_list() > 3.4036139000000003 sec
 append_deque() > 2.8610466 sec
                                        append_deque Быстрее чем append_list

 pop_list() > 0.050820100000000146 sec
 pop_deque() > 0.04757919999999949 sec
                                        pop_deque Быстрее чем pop_list

 extend_list() > 10.4405063 sec
 extend_deque() > 8.7639255 sec
                                        extend_deque Быстрее чем extend_list


2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

insert_list() > 1.3840755000000016 sec
append_left_deque() > 0.029689299999997587 sec
                                        append_left_deque значительно быстрее чем insert_list()

 pop_left_list() > 9.860434600000001 sec
 pop_left_deque() > 0.07986389999999943 sec
                                        pop_left_deque значительно быстрее чем  pop_left_list()

 extend_left_list() > 13.058909399999997 sec
 extend_left_deque() > 0.010025699999999915 sec
                                        extend_left_deque значительно быстрее чем insert_list()

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

 get_from_list() > 1.7381692000000015 sec
 get_from_deque() > 2.2365820999999997 sec
                                        get_from_list() Быстрее чем get_from_deque()

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.

script listing приложен ниже кода
"""
from collections import deque
from timeit import timeit


def append_list():
    gen_lst = []
    for i in range(100):
        gen_lst.append(i)
    return gen_lst


def append_deque():
    gen_deq = deque([])
    for i in range(100):
        gen_deq.append(i)
    return gen_deq


def pop_list(inp_list):
    while inp_list:
        a = inp_list.pop()


def pop_deque(inp_deq):
    while inp_deq:
        a = inp_deq.pop()


def extend_list(inp_list):
    for i in range(100):
        inp_list.extend(['a', 'b', 'c'])
    return


def extend_deque(inp_deq):
    for i in range(100):
        inp_deq.extend(['a', 'b', 'c'])
    return


def insert_list(inp_list):
    for i in range(10):
        inp_list.insert(0, i)
    return


def append_left_deque(inp_deq):
    for i in range(100):
        inp_deq.appendleft(i)
    return


def pop_left_list(inp_list):
    while inp_list:
        a = inp_list.pop(0)
    return


def pop_left_deque(inp_deq):
    while inp_deq:
        a = inp_deq.popleft()
    return


def extend_left_list(inp_list):
    for i in range(100):
        for j in ['a', 'b', 'c']:
            inp_list.insert(0, j)
    return


def extend_left_deque(inp_deq):
    for i in range(100):
        inp_deq.extendleft(['a', 'b', 'c'])
    return


def get_from_list(inp_list):
    for i in range(100):
        a = inp_list[i]
    return a


def get_from_deque(inp_deq):
    for i in range (100):
        a = inp_deq[i]
    return a




print(f'\n ---- Timing Measurements ---- ')

print(f' append_list() > {timeit("append_list()", globals=globals())} sec')
print(f' append_deque() > {timeit("append_deque()", globals=globals())} sec')

print('')
new_list = append_list()
new_deque = append_deque()
print(f' pop_list() > {timeit("pop_list(new_list)", globals=globals())} sec')
print(f' pop_deque() > {timeit("pop_deque(new_deque)", globals=globals())} sec')

print('')
print(f' extend_list() > {timeit("extend_list(new_list)", globals=globals())} sec')
print(f' extend_deque() > {timeit("extend_deque(new_deque)", globals=globals())} sec')

print('')
new_list = append_list()
new_deque = append_deque()
print(f' insert_list() > '
      f'{timeit("insert_list(new_list)", globals=globals(), number = 10000)} sec')
print(f' append_left_deque() > '
      f'{timeit("append_left_deque(new_deque)", globals=globals(), number = 10000)} sec')

print('')
print(f' pop_left_list() > {timeit("pop_left_list(new_list)", globals=globals())} sec')
print(f' pop_left_deque() > {timeit("pop_left_deque(new_deque)", globals=globals())} sec')

print('')
print(f' extend_left_list() > {timeit("extend_left_list(new_list)", globals=globals(), number = 1000)} sec')
print(f' extend_left_deque() > {timeit("extend_left_deque(new_deque)", globals=globals(), number = 1000)} sec')


print('')
print(f' get_from_list() > {timeit("get_from_list(new_list)", globals=globals())} sec')
print(f' get_from_deque() > {timeit("get_from_deque(new_deque)", globals=globals())} sec')


# Script listing
#
#
#  ---- Timing Measurements ----
#  append_list() > 3.4036139000000003 sec
#  append_deque() > 2.8610466 sec
#
#  pop_list() > 0.050820100000000146 sec
#  pop_deque() > 0.04757919999999949 sec
#
#  extend_list() > 10.4405063 sec
#  extend_deque() > 8.7639255 sec
#
#  insert_list() > 1.3840755000000016 sec
#  append_left_deque() > 0.029689299999997587 sec
#
#   pop_left_list() > 9.860434600000001 sec
#   pop_left_deque() > 0.07986389999999943 sec
#
#  extend_left_list() > 13.058909399999997 sec
#  extend_left_deque() > 0.010025699999999915 sec
#
#  get_from_list() > 1.7381692000000015 sec
#  get_from_deque() > 2.2365820999999997 sec
#
# Process finished with exit code 0
