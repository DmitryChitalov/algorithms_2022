"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(dct, n):
    for i in range(n):
        dct[i] = f"{i}"


def fill_ordered_dict(ord_dct, n):
    for i in range(n):
        ord_dct[i] = f"{i}"


def change_dict(dct, n):
    for i in range(n):
        dct[i] = f"{i+1}"


def change_ordered_dict(ord_dct, n):
    for i in range(n):
        ord_dct[i] = f"{i+1}"


def get_dict(dct):
    item_dict = None
    for item in dct.items():
        item_dict = item


def get_ordered_dict(ord_dct):
    item_ordered_dict = None
    for item in ord_dct.items():
        item_ordered_dict = item


def pop_dict(dct, n):
    for i in range(n):
        dct.pop(i)


def pop_ordered_dict(ord_dct, n):
    for i in range(n):
        ord_dct.pop(i)


if __name__ == '__main__':
    dict_test = {}
    ordered_dict_test = OrderedDict()
    n_test = 5000000
    print('Время выполнения наполнения dict и OrderedDict')
    print(f"Для dict: {timeit('fill_dict(dict_test, n_test)', globals=globals(), number=1)}")
    print(f"Для OrderedDict: {timeit('fill_ordered_dict(ordered_dict_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения изменения элементов dict и OrderedDict')
    print(f"Для dict: {timeit('change_dict(dict_test, n_test)', globals=globals(), number=1)}")
    print(f"Для OrderedDict: {timeit('change_ordered_dict(ordered_dict_test, n_test)', globals=globals(), number=1)}")
    print('Время выполнения получения элементов dict и OrderedDict')
    print(f"Для dict: {timeit('get_dict(dict_test)', globals=globals(), number=1)}")
    print(f"Для OrderedDict: {timeit('get_ordered_dict(ordered_dict_test)', globals=globals(), number=1)}")
    print('Время выполнения удаления элементов dict и OrderedDict')
    print(f"Для dict: {timeit('pop_dict(dict_test, n_test)', globals=globals(), number=1)}")
    print(f"Для OrderedDict: {timeit('pop_ordered_dict(ordered_dict_test, n_test)', globals=globals(), number=1)}")

# Наполнение dict выполняется намного быстрее, чем OrderedDict.
# Изменение, получение и удаление элементов из dict выполняется также быстрее.
# OrderedDict есть смысл использовать, если нужно:
# явно показать, что важен порядок следования элементов;
# удалить и вернуть первую пару ключ-значение (метод .popitem(last=False));
# переместить элемент по ключу в начало или конец (метод .move_to_end()).

