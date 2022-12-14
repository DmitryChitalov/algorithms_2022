"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

usual_dict = {}
ordered_dict = OrderedDict()


def fill_dict(dictionary, n):
    for i in range(n):
        dictionary[i] = i


print('Заполнение:')
print('Обычный словарь -', timeit(f'fill_dict({usual_dict}, {200})', globals=globals()))
print('-'*100)
print('OrderedDict', timeit(f'fill_dict({ordered_dict}, {200})', globals=globals()))
print('-'*100)
fill_dict(usual_dict, 100)
fill_dict(ordered_dict, 100)
print()
"""
Результаты:
Обычный словарь - 8.494062599995232
----------------------------------------------------------------------------------------------------
OrderedDict 16.01870059999783
----------------------------------------------------------------------------------------------------
OrderedDict заполняется медленнее
"""
def pop_dict(dictionary):
    for i in range(100):
        dictionary.pop(i)


print('Удаление:')
print('Обычный словарь -', timeit(f'pop_dict({usual_dict})', globals=globals()))
print('-'*100)
print('OrderedDict', timeit(f'pop_dict({ordered_dict})', globals=globals()))
print('-'*100)
print()

"""
Результаты:
Обычный словарь - 10.736174199999368
----------------------------------------------------------------------------------------------------
OrderedDict 17.985551500001748
----------------------------------------------------------------------------------------------------
Из OrderedDict элементы удаляются медленнее
"""
def change_dict(dictionary):
    for i in range(100):
        dictionary[i] = 'changed'


print('Изменение:')
print('Обычный словарь -', timeit(f'change_dict({usual_dict})', globals=globals()))
print('-'*100)
print('OrderedDict', timeit(f'change_dict({ordered_dict})', globals=globals()))
print('-'*100)
"""
Результаты:
Обычный словарь - 9.100728100005654
----------------------------------------------------------------------------------------------------
OrderedDict 14.628222899998946
----------------------------------------------------------------------------------------------------
В OrderedDict элементы изменяются медленнее
"""

"""
Выводы:
Если нет необходимости использовать специальные функции OrderedDict 
или сравнивать порядок в словарях, использовать OrderedDict нецелесообразно."""