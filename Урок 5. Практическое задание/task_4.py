"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

o_dct = OrderedDict()
dct = dict()

print('Заполнение словарей')
print(timeit('for i in range(1000): o_dct[i] = i', globals=globals(), number=1000))
print(timeit('for i in range(1000): dct[i] = i', globals=globals(), number=1000))

print('Получение значений по ключу')
print(timeit('for i in range(1000): a = o_dct[i]', globals=globals(), number=1000))
print(timeit('for i in range(1000): b = dct[i]', globals=globals(), number=1000))

print('Удаление элемента')
print(timeit('for _ in range(10): o_dct.popitem()', globals=globals(), number=100))
print(timeit('for _ in range(10): dct.popitem()', globals=globals(), number=100))

"""
Словари работают практически одинаково, с версии Python 3.6 
словарь упорядочивает элементы автоматически, необходимости
использовать OrderDict нет.

Заполнение словарей
OrderDict 0.007270900008734316
dict 0.007473499979823828
Получение значений по ключу
OrderDict 0.004161999968346208
dict 0.004891099990345538
Удаление элемента
OrderDict 0.00015310000162571669
dict 0.00010259996633976698
"""
