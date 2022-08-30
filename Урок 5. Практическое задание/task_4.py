"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
import timeit
test_ord_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8)])
test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


a = timeit.timeit("test_dict.get('c')", globals=globals(), number=1000)
b = timeit.timeit("test_ord_dict.get('c')", globals=globals(), number=1000)

print(f"""Время выполнения test_dict.get: {a} """)
print(f"""Время выполнения test_ord_dict.get: {b} """)
if a < b:
    print(f"""Время выполнения test_dict.get быстрее выполнения test_ord_dict.get на: {(b-a)/a*100}%""")
else:
    print(f"""Время выполнения test_ord_dict.get быстрее выполнения test_dict.get на: {(a-b)/b*100}%""")
"""
Ответ: #
"""
print()


a = timeit.timeit("test_dict.keys()", globals=globals(), number=1000)
b = timeit.timeit("test_ord_dict.keys()", globals=globals(), number=1000)
print(f"""Время выполнения test_dict.keys(): {a} """)
print(f"""Время выполнения test_ord_dict.keys(): {b} """)
if a < b:
    print(f"""Время выполнения test_dict.keys() быстрее выполнения test_ord_dict.keys() на: {(b-a)/a*100}%""")
else:
    print(f"""Время выполнения test_ord_dict.keys() быстрее выполнения test_dict.keys() на: {(a-b)/b*100}%""")
"""
Ответ: #
"""
print()


a = timeit.timeit("test_dict.update({'z': 26})", globals=globals(), number=1000)
b = timeit.timeit("test_ord_dict.update(OrderedDict([('z', 26)]))", globals=globals(), number=1000)
print(f"""Время выполнения test_dict.update(): {a} """)
print(f"""Время выполнения test_ord_dict.update(): {b} """)
if a < b:
    print(f"""Время выполнения test_dict.update быстрее выполнения test_ord_dict.update() на: {(b-a)/a*100}%""")
else:
    print(f"""Время выполнения test_ord_dict.update() быстрее выполнения test_dict.update на: {(a-b)/b*100}%""")
"""
Ответ: #
"""
print()
