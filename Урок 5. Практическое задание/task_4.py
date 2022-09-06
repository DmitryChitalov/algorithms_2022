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
import time


def waiting():
    f_sec = 3
    for _ in range(f_sec):
        if f_sec == 1:
            print(f'Производим расчёты. Результаты будут через: {f_sec} секунду.')
        else:
            print(f'Производим расчёты. Результаты будут через: {f_sec} секунды.')
        f_sec -= 1
        time.sleep(1)


tests_number = 1000000

just_dict = {}
ordered_dict_1 = OrderedDict()

print('- > Добавление элементов')
waiting()
print('    dict:', end=' ')
print(timeit('for i in range(tests_number):'
             '  just_dict[i] = (randrange(0,tests_number))', globals=globals(), number=1))
print('    ordered_dict:', end=' ')
print(timeit('for i in range(tests_number):'
             '  ordered_dict_1[i] = (randrange(0,tests_number))', globals=globals(), number=1))


print('\n- > Удаление элемента по ключу')
waiting()
print('    dict:', end=' ')
print(timeit('for i in range(tests_number // 2):'
             '  just_dict.pop(i)', globals=globals(), number=1))
print('    ordered_dict:', end=' ')
print(timeit('for i in range(tests_number // 2):'
             '  ordered_dict_1.pop(i)', globals=globals(), number=1))

print('\n- > Удаление последнего элемента')
waiting()
print('    dict:', end=' ')
print(timeit('just_dict.popitem()', globals=globals(), number=tests_number // 2))
print('    ordered_dict:', end=' ')
print(timeit('ordered_dict_1.popitem()', globals=globals(), number=tests_number // 2))

for i in range(tests_number//2):
    ordered_dict_1[i] = (randrange(0, tests_number))

print('\nУдаление первого элемента dict невозможно. А вот в OrderedDict очень даже. (ключ - False)')
waiting()
print('    ordered_dict:', end=' ')
print(timeit('ordered_dict_1.popitem(False)', globals=globals(), number=tests_number // 2))

just_dict_2 = dict()
ordered_dict_2 = OrderedDict()

for i in range(tests_number):
    just_dict[i] = just_dict_2[i] = ordered_dict_1[i] = ordered_dict_2[i] = (randrange(0, tests_number))

print('\n- > Сравнение словарей')
waiting()
print('    dict:', end=' ')
print(timeit('just_dict == just_dict_2', globals=globals(), number=10))
print('    ordered_dict:', end=' ')
print(timeit('ordered_dict_1 == ordered_dict_2', globals=globals(), number=10))


print('\n- > Получение элемента по ключу')
waiting()
print('    dict:', end=' ')
print(timeit('for i in range(tests_number):'
             '  just_dict.get(i)', globals=globals(), number=1))
print('    ordered_dict:', end=' ')
print(timeit('for i in range(tests_number):'
             '  ordered_dict_1.get(i)', globals=globals(), number=1))


"""
АНАЛИТИКА
Упорядоченный словарь работает медленнее, чем обычный. 
При этом в нём можно удалить первый элемент, что невозможно сделать в обычном словаре.
"""
