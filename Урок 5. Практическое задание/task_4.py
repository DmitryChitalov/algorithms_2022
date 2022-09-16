"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict
from random import randrange

randon_keys = list(range(0, 100000))
check_the_dict = {}
for i in randon_keys:
    check_the_dict[str(i)] = randrange(100000)

check_the_ordered_dict = OrderedDict()
for i in randon_keys:
    check_the_ordered_dict[str(i)] = randrange(100000)

# Проверяем добавление элемента

print(timeit("check_the_dict['100001'] = 0", number=10 ** 6, globals=globals()))
print(timeit("check_the_ordered_dict['100001'] = 0", number=10 ** 6, globals=globals()))

"""Результаты измерений:
Обычный словарь: 0.06090120000044408
Упорядоченный словарь OrderedDict: 0.10064360000069428
"""

# Проверяем изменения элемента

print(timeit("check_the_dict['10'] = 305", number=10 ** 6, globals=globals()))
print(timeit("check_the_ordered_dict['10'] = 305", number=10 ** 6, globals=globals()))

"""Результаты измерений:
Обычный словарь: 0.05740510000032373
Упорядоченный словарь OrderedDict: 0.09196239999982936
"""

# Получение ключей

print(timeit("check_the_dict.keys()", number=10 ** 6, globals=globals()))
print(timeit("check_the_ordered_dict.keys()", number=10 ** 6, globals=globals()))

"""Результаты измерений:
Обычный словарь: 0.07388779999928374
Упорядоченный словарь OrderedDict: 0.07181239999954414
"""

# Получение значений

print(timeit("check_the_dict.values()", number=10 ** 6, globals=globals()))
print(timeit("check_the_ordered_dict.values()", number=10 ** 6, globals=globals()))

"""Результаты измерений:
Обычный словарь: 0.07886110000072222
Упорядоченный словарь OrderedDict: 0.07223569999950996
"""

# Удаление значений

print(timeit("check_the_dict.popitem()", number=10 ** 5, globals=globals()))
print(timeit("check_the_ordered_dict.popitem()", number=10 ** 5, globals=globals()))

"""Результаты измерений:
Обычный словарь: 0.017425599999114638
Упорядоченный словарь OrderedDict: 0.026049199999761186
"""
"""
Измерения показывают, что в 3 случаях из 5 обычный словарь отрабатывает быстрее на 30-50 процентов (Python 3.10). 
В 2ух случаях из 5 в которых быстрее OrderedDict, разница незначительная. Меньше 10 процентов. 
Отсюда можно сделать вывод, что использовать OrderedDict в версиях выше Python 3.6 не имеет смысла.
"""