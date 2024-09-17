"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from email.policy import default
import numbers
from timeit import timeit
from random import shuffle


di = {i:i for i in range(100)}
od = OrderedDict(di.copy())
test_list = [i for i in range(10,40)]
shuffle(test_list)
test_di = {i:i**2 for i in range(1000,1100)}


d_get = timeit('''
for i in test_list:
    res = di.get(i)
''', globals=globals(), number=1000)

o_get = timeit('''
for i in test_list:
    res = od.get(i)
''', globals=globals(), number=1000)


d_pop = timeit('''
for i in test_list:
    di.pop(i)
''', globals=globals(), number=1)


o_pop = timeit('''
for i in test_list:
    od.pop(i)
''', globals=globals(), number=1)


o_val = timeit('''
res = od.values()
''', globals=globals(), number=1000)


d_val = timeit('''
res = di.values()
''', globals=globals(), number=1000)

o_update = timeit('''
od.update(test_di)
''', globals=globals(), number=1000)

d_update = timeit('''
di.update(test_di)
''', globals=globals(), number=1000)




# тестироване 
print(d_get)  # 0.002310128000090117
print(o_get)  # 0.002512518999992608

print(d_val)  # 5.0100999942515045e-05
print(o_val)  # 5.729100030293921e-05

print(d_update)  # 0.0013391090001277917
print(o_update)  # 0.00883061100012128

print(d_pop)  # 2.939999831141904e-06
print(o_pop)  # 6.309999662335031e-06

'''во всех случаях применения встроенных функций словарь
отрабатывает быстрее значит
Нет смысла исп-ть OrderedDict в Python 3.6 и более поздних версиях
максимум только для обозначения
что значения словаря должны быть упорядочены)'''