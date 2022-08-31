"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

dicts = {}
new_dict = OrderedDict(dicts)


# print(dicts)
# print(new_dict)

def dict_for(n):
    for k in range(0, 1005):
        n[k] = k * 2
    return f''


print(dict_for(dicts))
print(dict_for(new_dict))
print('dict for up', timeit('dict_for(dicts)', number=10000, globals=globals()))
print('orderdict for up', timeit('dict_for(new_dict)', number=10000, globals=globals()))
# по замерам dict немного быстрее


def popitem_dict(x):
    return x.popitem()


print('dict popitem', timeit('popitem_dict(dicts)', number=1000, globals=globals()))
print('order popitem', timeit('popitem_dict(new_dict)', number=1000, globals=globals()))
# по замерам dict немного быстрее


# Вы со мной будете не согласны, но особого смысла в поздних версиях Python в Orderdict не вижу.
# Есть специализированные задачи, но в большинстве случаев я буду использовать dict. 
# Очень понравилась эта статья https://www.awesomeandrew.ru/2021/07/10/ordereddict-vs-dict-%D0%B2-python-%D0%B2%D1%8B%D0%B1%D0%B8%D1%80%D0%B0%D0%B5%D0%BC-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD/
