"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from random import randint
from collections import OrderedDict
from timeit import timeit

classic_dict = {i: randint(0, 100) for i in range(1000)}
ordered_dict = OrderedDict({i: randint(0, 100) for i in range(1000)})


def t_dict_get(dt, count=50):
    result = ''
    for i in range(count):
        result += str(dt.get(randint(0, len(dt) - 1)))
    return dt


def t_orddict_get(odt, count=50):
    result = ''
    for i in range(count):
        result += str(odt.get(randint(0, len(odt) - 1)))
    return odt


def t_dict_update(dt, count=100):
    dt.update([(i, randint(0, count)) for i in range(101, count * 300)])
    return dt


def t_orddict_update(odt, count=100):
    odt.update([(i, randint(0, count)) for i in range(101, count * 300)])
    return odt


def t_dict_popitem(dt, count=100):
    for i in range(count):
        dt.popitem()
    return dt


def t_orddict_popitem(odt, count=100):
    for i in range(count):
        odt.popitem()
    return odt


def t_dict_pop(dt, count=100):
    for i in range(count):
        dt.pop(randint(0, len(dt) - 1), None)
    return dt


def t_orddict_pop(odt, count=100):
    for i in range(count):
        odt.pop(randint(0, len(odt) - 1), None)
    return odt


print(f'Время для classic_dict.get = '
      f'{timeit("t_dict_get(classic_dict)", globals=globals(), number=10000)}')
print(f'Время для ordered_dict.get = '
      f'{timeit("t_orddict_get(ordered_dict)", globals=globals(), number=10000)}')

print(f'Время для classic_dict.update = '
      f'{timeit("t_dict_update(classic_dict)", globals=globals(), number=100)}')
print(f'Время для ordered_dict.update = '
      f'{timeit("t_orddict_update(ordered_dict)", globals=globals(), number=100)}')

print(f'Время для classic_dict.popitem = '
      f'{timeit("t_dict_popitem(classic_dict)", globals=globals(), number=100)}')
print(f'Время для ordered_dict.popitem = '
      f'{timeit("t_orddict_popitem(ordered_dict)", globals=globals(), number=100)}')

print(f'Время для classic_dict.pop = '
      f'{timeit("t_dict_pop(classic_dict)", globals=globals(), number=100)}')
print(f'Время для ordered_dict.pop = '
      f'{timeit("t_orddict_pop(ordered_dict)", globals=globals(), number=100)}')

"""
Время для classic_dict.get = 0.2780831020008918
Время для ordered_dict.get = 0.2829708789995493
Время для classic_dict.update = 1.2254383170002257
Время для ordered_dict.update = 1.3251809390003473
Время для classic_dict.popitem = 0.00044365800022205804
Время для ordered_dict.popitem = 0.0007402810006169602
Время для classic_dict.pop = 0.006044395000571967
Время для ordered_dict.pop = 0.006202119000590756

Результаты всех тестов сопоставимы. Разница есть только в popitem.
Popitem в OrderedDict также позволяет определять с какого конца идёт удаление.
Начиная с версии 3.6 (с версии 3.7 это отдельно описано) обычный словарь запоминает порядок вставки.
Таким образом глобальных отличий по скорости работы в последних версиях python между dict и OrderedDict нет.
"""
