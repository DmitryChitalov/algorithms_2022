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
from random import randint
from collections import deque
from timeit import timeit

test_list = []
test_degue = deque([])


def t_l_append(lst, count=10000):
    for i in range(count):
        lst.append(i)
    return lst


def t_d_append(deg, count=10000):
    for i in range(count):
        deg.append(i)
    return deg


def t_l_pop(lst, count=100):
    for i in range(count):
        lst.pop()
    return lst


def t_d_pop(deg, count=100):
    for i in range(count):
        deg.pop()
    return deg


def t_l_extend(lst, count=100):
    for i in range(count):
        lst.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    return lst


def t_d_extend(deg, count=100):
    for i in range(count):
        deg.extend(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    return deg


def t_l_insert_start(lst, count=100):
    for i in range(count):
        lst.insert(0, i)
    return lst


def t_d_appendleft(deg, count=100):
    for i in range(count):
        deg.appendleft(i)
    return deg


def t_l_pop_start(lst, count=100):
    for i in range(count):
        lst.pop(0)
    return lst


def t_d_popleft(deg, count=100):
    for i in range(count):
        deg.popleft()
    return deg


def t_l_extend_cycle(lst, count=10):
    abc_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(count):
        for el in abc_list:
            lst.insert(0, el)
    return lst


def t_d_extendleft(deg, count=10):
    for i in range(count):
        deg.extendleft(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    return deg


def t_l_get_el(lst, count=100):
    result = ''
    for i in range(count):
        result += str(lst[randint(0, len(lst) - 1)])
    return lst


def t_d_get_el(deg, count=100):
    result = ''
    for i in range(count):
        result += str(deg[randint(0, len(deg) - 1)])
    return deg


print(f'Время для list.append = '
      f'{timeit("t_l_append(test_list)", setup="from __main__ import t_l_append, test_list", number=100)}')
print(f'Время для degue.append = '
      f'{timeit("t_d_append(test_degue)", setup="from __main__ import t_d_append, test_degue", number=100)}')

print(f'Время для list.pop = '
      f'{timeit("t_l_pop(test_list)", setup="from __main__ import t_l_pop, test_list", number=100)}')
print(f'Время для degue.pop = '
      f'{timeit("t_d_pop(test_degue)", setup="from __main__ import t_d_pop, test_degue", number=100)}')

print(f'Время для list.extend = '
      f'{timeit("t_l_extend(test_list)", setup="from __main__ import t_l_extend, test_list", number=100)}')
print(f'Время для degue.extend = '
      f'{timeit("t_d_extend(test_degue)", setup="from __main__ import t_d_extend, test_degue", number=100)}')

print(f'Время для list.insert_start = '
      f'{timeit("t_l_insert_start(test_list)", setup="from __main__ import t_l_insert_start, test_list", number=100)}')
print(f'Время для degue.appendleft = '
      f'{timeit("t_d_appendleft(test_degue)", setup="from __main__ import t_d_appendleft, test_degue", number=100)}')

print(f'Время для list.pop_start = '
      f'{timeit("t_l_pop_start(test_list)", setup="from __main__ import t_l_pop_start, test_list", number=100)}')
print(f'Время для degue.popleft = '
      f'{timeit("t_d_popleft(test_degue)", setup="from __main__ import t_d_popleft, test_degue", number=100)}')

print(f'Время для list.extend_cycle = '
      f'{timeit("t_l_extend_cycle(test_list)", setup="from __main__ import t_l_extend_cycle, test_list", number=100)}')
print(f'Время для degue.extendleft = '
      f'{timeit("t_d_extendleft(test_degue)", setup="from __main__ import t_d_extendleft, test_degue", number=100)}')

print(f'Время для list.get_el = '
      f'{timeit("t_l_get_el(test_list)", setup="from __main__ import t_l_get_el, test_list", number=1000)}')
print(f'Время для degue.get_el = '
      f'{timeit("t_d_get_el(test_degue)", setup="from __main__ import t_d_get_el, test_degue", number=1000)}')

"""
-------------------------------------------------------------1----------------------------------------------------------
Время для list.append  = 0.0340906340006768
Время для degue.append = 0.03549423299955379
Время для list.pop  = 0.0002478019996488001
Время для degue.pop = 0.0002413300007901853
Время для list.extend  = 0.0011712750001606764
Время для degue.extend = 0.0021199650000198744

append и pop выполняются за сопоставимое время.
extend для list выполняется в два раза быстрее, чем для degue. 
Возможно, это связано с тем, что при добавлении к degue расходуется время на приведение к degue.
К сожалению, из документации это не ясно: "Extend the right side of the deque with elements from the iterable."

-------------------------------------------------------------2----------------------------------------------------------
Время для list.insert_start = 2.236269242000162
Время для degue.appendleft = 0.0002712460000111605
Время для list.pop_start = 1.4374730799995632
Время для degue.popleft = 0.0002476919999025995
Время для list.extend_cycle = 5.8131357209999805
Время для degue.extendleft = 0.00026847099979931954

Во всех случаях degue показал себя на 4 порядка быстрее, чем list.
Degue оптимизирован для работы с конечными значениями, тогда как list больше подходит для "случайного" доступа.

-------------------------------------------------------------3----------------------------------------------------------
Время для list.get_el = 0.0661772089997612
Время для degue.get_el = 0.8784474340000088

Degue на порядок медленнее, чем list по той же причине, которая указана для второй группы тестов:
Degue (колода) совмещает в себе плюсы принципов LIFO и FIFO, что "облегчает" доступ к конечным значениям, тогда как
list оптимизирован для рандомного доступа к элементам.

"""
