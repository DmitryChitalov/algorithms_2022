"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import timeit
import collections

diction = {}
order_diction = collections.OrderedDict()

for i in range(1000, 1, -1):
    diction[i] = i

for i in range(1000, 1, -1):
    order_diction[i] = i

test = """
for i in range(1000, 1, -1):
    diction[i] = i
"""

print("Замеры с обычным словарем", timeit.timeit(test, number=10000, globals=globals()))

test2 = """
for i in range(1000, 1, -1):
    order_diction[i] = i
"""
print("Замеры с OrderDict словарем", timeit.timeit(test2, number=10000, globals=globals()))
'''
Добавления информации в обычный словарь осуществляется с незначительным приростом скорости, на небольших 
объемах информации этого заметно не будет
'''

"""
Тест 2
"""
print("замеры 2")
print("Замеры с обычным словарем", timeit.timeit("diction[300]", number=100000, globals=globals()))
print("Замеры с сортированным словарем", timeit.timeit("order_diction[300]", number=100000, globals=globals()))
'''
Получения информации в сортированном словарь осуществляется с незначительным приростом скорости, на небольших 
объемах информации этого заметно не будет
'''

"""
Тест 3
"""
print("замеры 3")
print("Замеры с обычным словарем", timeit.timeit("sorted(diction.keys())", number=100000, globals=globals()))
print("Замеры с сортированным словарем",
      timeit.timeit("sorted(order_diction.keys())", number=100000, globals=globals()))
'''
Сортировка отсортированного словаря происходит очень долго практически в два раза
Большо смысла в использовании отсортированных словарей нет, так как в обычных операциях нет больго прироста скорости
'''
