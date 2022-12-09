"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

dict1 = {
    "name": "Ivan",
    "surname": "Ivanov",
    "age": 25,
    "city": "Moscow",
    "profession": "doctor"
}
print(dict1)

dict2 = OrderedDict(dict1)
print(dict2)

print('\nСравнение операции pop обычного словаря и упорядоченного словаря OrderedDict')
print(timeit('dict1.pop("name")', globals=globals(), number=1))
print(timeit('dict2.pop("name")', globals=globals(), number=1))

print('\nСравнение операции popitem обычного словаря и упорядоченного словаря OrderedDict')
print(timeit('dict1.popitem()', globals=globals(), number=1))
print(timeit('dict2.popitem()', globals=globals(), number=1))

print('\nДобавление нового элемента в обычный словарь и упорядоченный словарь OrderedDict')
print(timeit('dict1["status"] = "married"', globals=globals(), number=1))
print(timeit('dict2["status"] = "married"', globals=globals(), number=1))

print('\nПолучение значения по ключу у обычного словаря и упорядоченного словаря OrderedDict')
print(timeit('dict1["surname"]', globals=globals(), number=1))
print(timeit('dict2["surname"]', globals=globals(), number=1))

print('\nИзменение содержимого значения у обычного словаря и упорядоченного словаря OrderedDict')
print(timeit('dict1["age"] = 26', globals=globals(), number=1))
print(timeit('dict2["age"] = 26', globals=globals(), number=1))

print('\nОчистка обычного словаря и упорядоченного словаря OrderedDict')
print(timeit('dict1.clear()', globals=globals(), number=1))
print(timeit('dict2.clear()', globals=globals(), number=1))

'''Все вышеуказанные операции, кроме операции получения элемента по ключу, у обычного словаря выполняется
быстрее, чем у упорядоченного словаря OrderedDict. Операция получения элемента по ключу у обычного словаря 
и у упорядоченного словаря OrderedDict выполняется с одинаковой скоростью.
Cмысла использовать OrderedDict в Python 3.6 и более поздних версиях нет, так как обычный словать тоже имеет
возможность запоминать порядок вставки элементов, а все основные операции у обычного словаря выполняются
быстрее, чем у упорядоченного словаря OrderedDict'''
