"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


odict = OrderedDict()
sdict = dict()


# Добавлене ключей
print('Добавление ключей')
print(timeit('for i in range(10000000):'
             '  odict[i] = i', globals=globals(), number=1))
print(timeit('for i in range(10000000):'
             '  sdict[i] = i', globals=globals(), number=1))

# Поиск по ключу
print('Поиск по ключу')
print(timeit('for i in range(10000000):'
             '  odict[i]', globals=globals(), number=1))
print(timeit('for i in range(10000000):'
             '  sdict[i]', globals=globals(), number=1))

# Удаление ключей
print('Удаление ключей')
print(timeit('for i in range(10000000):'
             '  odict.pop(i)', globals=globals(), number=1))
print(timeit('for i in range(10000000):'
             '  sdict.pop(i)', globals=globals(), number=1))

"""
Добавление ключей
    1.4237875000108033
    0.9536890001036227
Поиск по ключу
    0.6417443999089301
    0.618559799855575
Удаление ключей
    1.8898720000870526
    1.1097957000602037

По всем основным операциям OrderedDict проигрывает и занимает больше памяти, но все еще актуален в случаях, когда:

1. необходимо сделать акцент в коде на то, что порядок словаря важен
2. нужно переупорядочить элементы в словаре. Можно использовать методы .move_to_end() и расширенный вариант 
    .popitem(), который позволяет забирать элементы не только с конца, но и с начала.
3. при сравнении словарей важно сравнивать не только их содержимое, но и порядок следования ключей
"""