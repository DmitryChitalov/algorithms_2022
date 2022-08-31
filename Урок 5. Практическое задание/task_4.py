"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit
from random import randrange

tests_number = 1000000

just_dict = {}
my_ordered_dict = OrderedDict()

print('Добавление элементов')
print('dict', end=' ')
print(timeit('for i in range(tests_number):'
             '  just_dict[i] = (randrange(0,tests_number))', globals=globals(), number=1))
print('ordered_dict', end=' ')
print(timeit('for i in range(tests_number):'
             '  my_ordered_dict[i] = (randrange(0,tests_number))', globals=globals(), number=1))

print('Удаление элемента по ключу')
print('dict', end=' ')
print(timeit('for i in range(tests_number // 2):'
             '  just_dict.pop(i)', globals=globals(), number=1))
print('ordered_dict', end=' ')
print(timeit('for i in range(tests_number // 2):'
             '  my_ordered_dict.pop(i)', globals=globals(), number=1))

print('Удаление последнего элемента')
print('dict', end=' ')
print(timeit('just_dict.popitem()', globals=globals(), number=tests_number // 2))
print('ordered_dict', end=' ')
print(timeit('my_ordered_dict.popitem()', globals=globals(), number=tests_number // 2))

for i in range(tests_number//2):
    my_ordered_dict[i] = (randrange(0, tests_number))

print('Удаление первого элемента')
print('в dict невозможно')
print('ordered_dict', end=' ')
print(timeit('my_ordered_dict.popitem(False)', globals=globals(), number=tests_number // 2))

just_dict_2 = dict()
my_ordered_dict_2 = OrderedDict()

for i in range(tests_number):
    just_dict[i] = just_dict_2[i] = my_ordered_dict[i] = my_ordered_dict_2[i] = (randrange(0, tests_number))

print('Сравнение словарей')
print('dict', end=' ')
print(timeit('just_dict == just_dict_2', globals=globals(), number=10))
print('ordered_dict', end=' ')
print(timeit('my_ordered_dict == my_ordered_dict_2', globals=globals(), number=10))

print('Получение элемента по ключу')
print('dict', end=' ')
print(timeit('for i in range(tests_number):'
             '  just_dict.get(i)', globals=globals(), number=1))
print('ordered_dict', end=' ')
print(timeit('for i in range(tests_number):'
             '  my_ordered_dict.get(i)', globals=globals(), number=1))
'''
Упорядоченный словарь работает медленнее, чем обычный. 
При этом в нём можно удалить первый элемент, что невозможно сделать в обычном словаре.
'''