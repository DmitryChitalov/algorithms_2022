"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit


def fill_dict(num):
    return dict.fromkeys(range(num))


def fill_ordered_dict(num):
    return OrderedDict.fromkeys(range(num))


n = 10
my_dict = fill_dict(n)
my_ordered_dict = fill_ordered_dict(n)

print(f'Время заполнения fill_dict = {timeit("fill_dict(n)", globals=globals())}')
print(f'Время заполнения fill_ordered_dict = {timeit("fill_ordered_dict(n)", globals=globals())}')


def copy_dict():
    dict_1 = my_dict.copy()


def copy_ordered_dict():
    dict_1 = my_ordered_dict.copy()


print(f'Время копирования copy_dict = {timeit("copy_dict()", globals=globals())}')
print(f'Время копирования copy_ordered_dict = {timeit("copy_ordered_dict()", globals=globals())}')


def pop_dict():
    for i in range(len(dict_1)):
        dict_1.pop(i)


def pop_ordered_dict():
    for i in range(len(dict_1)):
        dict_1.pop(i)


dict_1 = my_dict.copy()
print(f'Время изъятия элемента pop_dict = {timeit("pop_dict()", globals=globals())}')
dict_1 = my_ordered_dict.copy()
print(f'Время изъятия элемента pop_ordered_dict = {timeit("pop_ordered_dict()", globals=globals())}')


def del_dict():
    for i in range(len(dict_1)):
        del dict_1[i]


def del_ordered_dict():
    for i in range(len(dict_1)):
        del dict_1[i]


dict_1 = my_dict.copy()
print(f'Время удаления элемента del_dict = {timeit("del_dict()", globals=globals())}')
dict_1 = my_ordered_dict.copy()
print(f'Время удаления элемента del_ordered_dict = {timeit("del_ordered_dict()", globals=globals())}')


def move_to_end_dict():
    for i in range(len(dict_1)):
        new = dict_1[i]
        del dict_1[i]
        dict_1[i] = new


def move_to_end_order_dict():
    for i in range(5):
        dict_1.move_to_end(i, False)


dict_1 = my_dict.copy()
print(f'Время перемещения элемента move_to_end_dict = {timeit("move_to_end_dict()", globals=globals())}')
dict_1 = my_ordered_dict.copy()
print(f'Время перемещения элемента move_to_end_order_dict = {timeit("move_to_end_order_dict()", globals=globals())}')


'''
OrderedDict значительно медлительнее чем словарь dict в операциях наполнения, копирования, небольшая потеря в скороти при 
изъятии и удалении элементов. Но имеется приимущество в случае использования .move_to_end().
в Python 3.6 и более поздних версиях есть смысл исп-ть OrderedDict по следующим причинам:

- Класс collections.OrderedDict() был разработан для частыx операций переупорядочивания. 
Эффективность использования памяти, скорость итераций и производительность операций обновления были второстепенными.

- Алгоритмически collections.OrderedDict() может обрабатывать частые операции переупорядочения лучше, чем обычный словарь dict. 
Это делает его подходящим для отслеживания недавних обращений например, в кеш LRU.

- Операция равенства для OrderedDict проверяет соответствие порядка ключей.

- Метод .popitem() класса OrderedDict() имеет другую сигнатуру. Он принимает необязательный аргумент, чтобы указать, какой элемент появляется.

- OrderedDict имеет метод .move_to_end() для эффективного перемещения элемента в конечную точку.

- До Python 3.8 в обычных словарях dict отсутствовал метод __reversed__().
'''

