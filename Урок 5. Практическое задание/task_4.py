"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
import timeit


d_1 = OrderedDict({x: x ** 2 for x in range(100000)})
d_2 = {x: x ** 2 for x in range(100000)}


def change_dct_1():
    for _ in d_1.copy():
        d_1.popitem()
    return d_1


def change_dct_2():
    for _ in d_2.copy():
        d_2.popitem()
    return d_2


print(timeit.timeit(
    stmt='d_1 = OrderedDict({x: x ** 2 for x in range(100)})',
    globals=globals(),
    number=1000))
print(timeit.timeit(
    stmt='d_2 = {x: x**2 for x in range(100)}',
    globals=globals(),
    number=1000))

print(timeit.timeit(
    stmt='change_dct_1()',
    globals=globals(),
    number=100))
print(timeit.timeit(
    stmt='change_dct_2()',
    globals=globals(),
    number=100))

#  Генерация упорядоченного словаря из коллекции происходит немного дольше:
#  0.02988529999999999 против 0.019441600000000003.
#  Удаление элементов с конца происходит быстрее в обычном словаре: 0.022958700000000026 против 0.008434300000000006.
#  Использование упорядоченного словаря требуется, когда нужно явно показать, что элементы в словаре упорядочены.
#  Это является актуальным до тех пор, пока в среде разработчиков используются версии интерпретатора < 3.6
#  либо используются программы, написанные на версиях ниже < 3.6.
#  Кроме того, OrderedDict предлагат альтернативные инструменты для работы со словарем, например, move_to_end.
