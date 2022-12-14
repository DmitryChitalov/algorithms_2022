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

from timeit import timeit, repeat, default_timer
from collections import deque
import re

my_list = list(range(1, 1001))
my_deque = deque(my_list)

def append_to_list(el):
    my_list.append(el)
    return

def append_to_deque(el):
    my_deque.append(el)
    return

def pop_from_list():
    my_list.pop()
    return

def pop_from_deque():
    my_deque.pop()
    return

def extend_list(extention):
    my_list.extend(extention)
    return

def extend_deque(extention):
    my_deque.extend(extention)
    return

def append_left_to_list(el):
    my_list.insert(0, el)
    return

def append_left_to_deque(el):
    my_deque.appendleft(el)
    return

def pop_left_from_list():
    my_list.pop(0)
    return

def pop_left_from_deque():
    my_deque.popleft()
    return

def extend_left_list(extention):
    my_list[:0] = extention
    return

def extend_left_deque(extention):
    my_deque.extendleft(extention)
    return

def get_el_from_list(el_to_find):
    if el_to_find in my_list:
        return el_to_find
    else:
        return 'Нет такого элемента'

def get_el_from_deque(el_to_find):
    if el_to_find in my_deque:
        return el_to_find
    else:
        return 'Нет такого элемента'

setup = '''
from random import randint
from __main__ import append_to_list, append_to_deque, pop_from_list, pop_from_deque, extend_list, extend_deque, append_left_to_list, append_left_to_deque, pop_left_from_list, pop_left_from_deque, extend_left_list, extend_left_deque, get_el_from_list, get_el_from_deque
el = randint(1, 2001)
extention = list(range(1, randint(1, 101)))
el_to_find = randint(100, 500)
'''

function_pairs = [
    ['append_to_list(el)', 'append_to_deque(el)'],
    ['pop_from_list()', 'pop_from_deque()'],
    ['extend_list(extention)', 'extend_deque(extention)'],
    ['append_left_to_list(el)', 'append_left_to_deque(el)'],
    ['pop_left_from_list()', 'pop_left_from_deque()'],
    ['extend_left_list(extention)', 'extend_left_deque(extention)'],
    ['get_el_from_list(el_to_find)', 'get_el_from_deque(el_to_find)']
    ]

def compare_functions(functions):
    print('COMPARING ' + re.findall(r'(.+?)\(', functions[0])[0] + ' AND ' + re.findall(r'(.+?)\(', functions[1])[0])
    for func in functions:
        result = repeat(func, setup, default_timer, 3, 1000)
        print(re.findall(r'(.+?)\(', func)[0] + ' - ' + str(min(result)))

for pair in function_pairs:
    compare_functions(pair)
    print('\n')


'''
Для всех функций сделала по 3 замера (по 1000 вызовов для каждого). В результатах выведен минимальный среди замеров.

Мои результаты:

ПУНКТ 1

COMPARING append_to_list AND append_to_deque
append_to_list - 0.00010512000153539702
append_to_deque - 0.00010694999946281314

COMPARING pop_from_list AND pop_from_deque
pop_from_list - 9.945000056177378e-05
pop_from_deque - 0.00010139000005437993

COMPARING extend_list AND extend_deque
extend_list - 0.00015435999739565887
extend_deque - 0.0006659099999524187

У append и pop примерно одинаковая скорость для списка и дека. extend отрабатывает быстрее для списка чем для дека.

ПУНКТ 2

COMPARING append_left_to_list AND append_left_to_deque
append_left_to_list - 0.020726460999867413
append_left_to_deque - 0.00011580900172702968

COMPARING pop_left_from_list AND pop_left_from_deque
pop_left_from_list - 0.008997600001748651
pop_left_from_deque - 7.603999983984977e-05

COMPARING extend_left_list AND extend_left_deque
extend_left_list - 0.014077460000407882
extend_left_deque - 0.0001518299977760762

Все три операции отрабатывают сильно быстрее для дека чем для функции. Это логично, потому что если

ПУНКТ 3

COMPARING get_el_from_list AND get_el_from_deque
get_el_from_list - 1.8938150880003377
get_el_from_deque - 3.64136508699994

Получение элемента отрабтывает быстрее для списка чем для дека

>
'''
