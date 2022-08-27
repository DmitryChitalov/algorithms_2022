"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


my_dict = {}
my_ordict = OrderedDict()


print('my_dict pop and [i] = i - ', timeit("""
for i in range(100):
    my_dict[i] = i
    my_dict.pop(i)""", globals=globals()))


print('my_ORdict pop and [i] = i - ', timeit("""
for i in range(100):
    my_ordict[i] = i
    my_ordict.pop(i)""", globals=globals()))

# my_dict pop and [i] = i - 38.106367500000005
# my_ORdict pop and [i] = i - 86.3746825


print('my_dict[i] = i - ', timeit("""
for i in range(100):
    my_dict[i] = i
    my_dict.popitem()""", globals=globals()))

print('my_ORdict[i] = i - ', timeit("""
for i in range(100):
    my_ordict[i] = i
    my_ordict.popitem()""", globals=globals()))

# my_dict[i] = i -  38.4979477
# my_ORdict[i] = i -  62.0599736

"""
Вывод:
        По скорости работы - стандартный dict быстрее.
        OrderedDict можно использовать, если нужно указать, что упорядоченность
        важна. Также в нем легко контроллировать порядок (move_to_end(), popitem()).
        Можно сравнивать полную эквивалентность словарей - важен порядок.
"""