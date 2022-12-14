"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit, repeat, default_timer
from collections import OrderedDict
import re

my_dict = {}
my_ordered_dict = OrderedDict()

# ЗАПОЛНЕНИЕ СЛОВАРЯ

def fill_dict():
    global my_dict
    for i in range(1, 1001):
        my_dict[i] = 'a' * i
    return

def fill_ordered_dict():
    global my_ordered_dict
    for i in range(1, 1001):
        my_ordered_dict[i] = 'a' * i
    return

# ДОБАВЛЕНИЕ КЛЮЧА В СЛОВАРЬ

def add_to_dict(key, value):
    global my_dict
    if key not in my_dict:
        my_dict[key] = value
    return

def add_to_ordered_dict(key, value):
    global my_ordered_dict
    if key not in my_ordered_dict:
        my_ordered_dict[key] = value
    return

# ДОБАВЛЕНИЕ КЛЮЧА В НАЧАЛО СЛОВАРЯ

def add_to_beginning_of_dict(key, value):
    global my_dict
    if key not in my_dict:
        end_part = my_dict
        my_dict = {key: value}
        my_dict.update(end_part)
    return

def add_to_beginning_of_ordered_dict(key, value):
    global my_ordered_dict
    if key not in my_ordered_dict:
        my_ordered_dict[key] = value
        my_ordered_dict.move_to_end(key, last=False)
    return

# УДАЛЕНИЕ КЛЮЧА

def delete_from_dict(key):
    global my_dict
    if key in my_dict:
        del my_dict[key]
    return

def delete_from_ordered_dict(key):
    global my_ordered_dict
    if key in my_ordered_dict:
        del my_ordered_dict[key]
    return

# ПОЛУЧЕНИЕ ЗНАЧЕНИЕ КЛЮЧА

def get_dict_value_by_key(key):
    global my_dict
    if key in my_dict:
        return my_dict[key]
    return 'Нет такого ключа'

def get_ordered_dict_value_by_key(key):
    global my_ordered_dict
    if key in my_ordered_dict:
        return my_ordered_dict[key]
    return 'Нет такого ключа'

# ПЕРЕМЕЩЕНИЕ КЛЮЧА В КОНЕЦ

def move_dict_key_to_end(key):
    global my_dict
    if key in my_dict:
        to_add = {key: my_dict[key]}
        del my_dict[key]
        my_dict.update(to_add)
    return 'Нет такого ключа'

def move_ordered_dict_key_to_end(key):
    global my_ordered_dict
    if key in my_ordered_dict:
        my_ordered_dict.move_to_end(key, last=True)
    return 'Нет такого ключа'

setup = '''
from random import randint
from __main__ import fill_dict, fill_ordered_dict, add_to_dict, add_to_ordered_dict, delete_from_dict, delete_from_ordered_dict, get_dict_value_by_key, get_ordered_dict_value_by_key, add_to_beginning_of_dict, add_to_beginning_of_ordered_dict, move_dict_key_to_end, move_ordered_dict_key_to_end
new_key = randint(1001, 2000)
new_value = 'a' * new_key
new_key_2 = randint(2001, 3000)
new_value_2 = 'a' * new_key_2
key_to_delete = randint(200, 800)
key_to_find = randint(1000, 1300)
key_to_move = randint(1000, 1300)
'''

function_pairs = [
    ['fill_dict()', 'fill_ordered_dict()'],
    ['add_to_dict(new_key, new_value)', 'add_to_ordered_dict(new_key, new_value)'],
    ['add_to_beginning_of_dict(new_key_2, new_value_2)', 'add_to_beginning_of_ordered_dict(new_key_2, new_value_2)'],
    ['delete_from_dict(key_to_delete)', 'delete_from_ordered_dict(key_to_delete)'],
    ['get_dict_value_by_key(key_to_find)', 'get_ordered_dict_value_by_key(key_to_find)'],
    ['move_dict_key_to_end(key_to_move)', 'move_ordered_dict_key_to_end(key_to_move)']
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
Мои результаты:

COMPARING fill_dict AND fill_ordered_dict
fill_dict - 0.08253478299957351
fill_ordered_dict - 0.10789817899785703


COMPARING add_to_dict AND add_to_ordered_dict
add_to_dict - 6.243999814614654e-05
add_to_ordered_dict - 6.349000250338577e-05


COMPARING add_to_beginning_of_dict AND add_to_beginning_of_ordered_dict
add_to_beginning_of_dict - 8.721999984118156e-05
add_to_beginning_of_ordered_dict - 6.299999949987978e-05


COMPARING delete_from_dict AND delete_from_ordered_dict
delete_from_dict - 6.055000267224386e-05
delete_from_ordered_dict - 6.241999653866515e-05


COMPARING get_dict_value_by_key AND get_ordered_dict_value_by_key
get_dict_value_by_key - 5.864999911864288e-05
get_ordered_dict_value_by_key - 5.8900001022266224e-05


COMPARING move_dict_key_to_end AND move_ordered_dict_key_to_end
move_dict_key_to_end - 6.036999911884777e-05
move_ordered_dict_key_to_end - 5.903999772272073e-05

В целом разница между замерами для аналогичных операций у словаря и OrderedDict небольшая.

Заполнение обычного словаря происходит суть быстрее, добавление ключа и значение в начало словаря и перемещения ключа в конец происходит быстрее для OrderedDict

Есть ли смысл использовать OrderedDict в Python 3.6 и более поздних версиях?

Да, если:

- хотите показать, что имеем дело с именно с упорядоченным словарем
- хотите перемещать элементы в начало/конец словаря - зраница в звмерах небольшая, но код выглядит чище для OrderedDict
'''
