"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

# Особого смысла использовать OrderedDict в Python 3.6 и более поздних версиях нет, потому как эти версии самостоятельно 
# делают словарь упорядоченными.

from timeit import timeit
from collections import OrderedDict

dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dict)

new_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(new_dict)

new_dict.move_to_end('b', last=True)
print(new_dict)

res = new_dict.popitem(last=True)
dict.popitem()
print(dict)
print('-' * 100)

print(res)
print(new_dict)
