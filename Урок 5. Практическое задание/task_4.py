"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {i: i for i in range(100)}
ord_dict = OrderedDict(simple_dict)

print(timeit('''for i in range(100):
                    simple_dict[i+100] = i''', 'from __main__ import simple_dict', number=1000))
print(timeit('''for i in range(100):
                    ord_dict[i+100] = i''', 'from __main__ import ord_dict', number=1000))
print(timeit('''for i in range(10):
                    simple_dict.popitem()''', 'from __main__ import simple_dict', number=10))
print(timeit('''for i in range(10):
                    ord_dict.popitem(last=True)''', 'from __main__ import ord_dict', number=10))
print(timeit('''for i in range(10):
                    el = simple_dict.pop(list(simple_dict)[0])
                    simple_dict[-1] = el''', 'from __main__ import simple_dict', number=1000))
print(timeit('''for i in range(10):
                    ord_dict.move_to_end(list(ord_dict)[0])''', 'from __main__ import ord_dict', number=1000))
'''
Операции OrderDict медленнее

0.010537000000000005
0.0187485

2.939999999999887e-05
7.91000000000125e-05

0.007947999999999997
0.0519169 
'''