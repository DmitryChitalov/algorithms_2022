"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

dct_ = dict()
order_dct = OrderedDict()
N = 1000  # Количество иттераций


# 1. Наполнение словаря
def filling(dct):
    for i, j in zip(range(N), range(N)):
        dct[i] = str(j)


# print(f'Наполнение обычного словаря: {timeit("filling(dct_)", globals=globals(), number=10000)}')
# print(f'Наполнение упорядоченного словаря: {timeit("filling(order_dct)", globals=globals(), number=10000)}')
'''
Наполнение обычного словаря: 2.012400900013745
Наполнение упорядоченного словаря: 2.2262721001170576

Упорядоченный словарь отрабатывает чуть медленнее
'''


# 2. Получение элемента по ключу
def get_(dct):
    for i in range(N):
        dct.get(i, None)


# print(f'Получение элемента для обычного словаря: {timeit("get_(dct_)", globals=globals(), number=10000)}')
# print(f'Получение элемента для упорядоченного словаря: {timeit("get_(order_dct)", globals=globals(), number=10000)}')
'''
Получение элемента для обычного словаря: 0.7187994997948408
Получение элемента для упорядоченного словаря: 0.9283108003437519

Упорядоченный словарь отрабатывает чуть медленнее
'''


# 3. Добавление словаря в словарь
def update_(dct):
    if isinstance(dct, dict):
        dct_upd = {i: str(j) for i, j in zip(range(N, 2 * N), range(N, 2 * N))}
        dct.update(dct_upd)
    else:
        dct_upd = OrderedDict({i: str(j) for i, j in zip(range(N, 2 * N), range(N, 2 * N))})
        dct.update(dct_upd)


# print(f'Обновление обычного словаря: {timeit("update_(dct_)", globals=globals(), number=10000)}')
# print(f'Обновление упорядоченного словаря: {timeit("update_(order_dct)", globals=globals(), number=10000)}')

'''
Обновление обычного словаря: 2.551622699946165
Обновление упорядоченного словаря: 3.1826008004136384
Упорядоченный словарь отрабатывает медленнее.
'''


# 4. Удаление последнего элемента
def popitem_(dct):
    if isinstance(dct, dict):
        dct = {i: str(j) for i, j in zip(range(N), range(N))}
    else:
        dct = OrderedDict({i: str(j) for i, j in zip(range(N), range(N))})
    for _ in range(N):
        dct.popitem()


# print(f'Popitem обычного словаря: {timeit("popitem_(dct_)", globals=globals(), number=10000)}')
# print(f'Popitem упорядоченного словаря: {timeit("popitem_(order_dct)", globals=globals(), number=10000)}')
'''
Popitem обычного словаря: 2.867581999860704
Popitem упорядоченного словаря: 2.636646999977529
Для упорядоченного словаря popitem отрабатывает быстрее
'''


# 5. Удаление элемента по ключу
def pop_(dct):
    if isinstance(dct, dict):
        dct = {i: str(j) for i, j in zip(range(N), range(N))}
    else:
        dct = OrderedDict({i: str(j) for i, j in zip(range(N), range(N))})
    for i in range(N):
        dct.pop(i, None)


# print(f'Pop обычного словаря: {timeit("pop_(dct_)", globals=globals(), number=10000)}')
# print(f'Pop упорядоченного словаря: {timeit("pop_(order_dct)", globals=globals(), number=10000)}')
'''
Pop обычного словаря: 3.0404052999801934
Pop упорядоченного словаря: 2.818497700151056
Удаление элемента по ключу так же отрабатывает быстрее у OrderedDict. 
'''

'''
Резюмируя всё вышенаписанное можно прийти к выводу, что упорядоченный словарь в большинстве случаев сильно уступает
обычному словарю, но у OrderedDict есть одно огромное преимущество, способное перекрыть нехватку скорости - 
добавление аттрибутов через конструктор класса
'''

ord_dct = OrderedDict(a=1, c=3, b=2)
print(ord_dct)
ord_dct.sorted_keys = lambda: sorted(ord_dct.keys())
for i in ord_dct.sorted_keys():
    print(ord_dct[i], end=' ')
print()
print(ord_dct.sorted_keys())
print(ord_dct.__dict__)

'''
OrderedDict([('a', 1), ('c', 3), ('b', 2)])
1 2 3 
['a', 'b', 'c']
{'sorted_keys': <function <lambda> at 0x00000238B8459510>}

Позволяет делать сортировку ключей и выводить их значения без измения изначального словаря.
Возможности у этого огромные, выше написан лишь простой пример.
'''
