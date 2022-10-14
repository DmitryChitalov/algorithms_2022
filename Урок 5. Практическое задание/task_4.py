"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit

reg_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
}

ordered_dict = OrderedDict([
    ('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)
])

results = {
    'reg_dict appoint':
        timeit('for k, v in reg_dict.items(): _, __ = k, v', globals=globals()),
    'ordered_dict appoint':
        timeit('for k, v in ordered_dict.items(): _, __ = k, v', globals=globals()),
    'reg_dict setdefault':
        timeit('for k in ordered_dict: reg_dict.setdefault(k, 6)', globals=globals()),
    'ordered_dict setdefault':
        timeit('for k in ordered_dict: ordered_dict.setdefault(k, 6)', globals=globals()),
    'reg_dict popitem':
        timeit('while len(reg_dict) != 0: reg_dict.popitem()', globals=globals()),
    'ordered_dict popitem':
        timeit('while len(ordered_dict) != 0: ordered_dict.popitem()', globals=globals()),
    'reg_dict update':
        timeit('for i in range(100): reg_dict.update({i: i + 1})', globals=globals()),
    'ordered_dict update':
        timeit('for i in range(100): ordered_dict.update({i: i + 1})', globals=globals()),

}

for k, v in results.items(): print(f'{k}: {v}')

'''
reg_dict appoint: 0.2728396630000134
ordered_dict appoint: 0.34236568999995143
reg_dict setdefault: 0.34308095300002606
ordered_dict setdefault: 0.34744075599996904
reg_dict popitem: 0.05453830099997958
ordered_dict popitem: 0.053471638000019084
reg_dict update: 13.073531344999992
ordered_dict update: 22.943993395000007
'''

# во всех случаях обычный словарь превосходит по скорости упорядоченный.
# уже исходя из этого, смысла в использовании упорядоченного нет