"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit

n = 1000
b_dict = {}
o_dict = OrderedDict()


def add_ordinary(n):
    for i in range(n):
        b_dict[i] = i


def add_ordered(n):
    for i in range(n):
        o_dict[i] = i


print(f'Наполнение обычного словаря элементами    '
      f'= {timeit("add_ordinary(n)", globals=globals(), number=10000)}')
print(f'Наполнение OrderedDict словаря элементами '
      f'= {timeit("add_ordered(n)", globals=globals(), number=10000)}')



def get_ordinary(n):
    for i in range(n):
        b_dict.get(i)


def get_ordered(n):
    for i in range(n):
        o_dict.get(i)


print(f'Получение элемента из обычного словаря    = '
      f'{timeit("get_ordinary(n)", globals=globals(), number=10000)}')
print(f'Получение элемента из OrderedDict словаря = '
      f'{timeit("get_ordered(n)", globals=globals(), number=10000)}')


def pop_ordinary():
    for i in range(len(b_dict)):
        b_dict.pop(i)


def pop_ordered():
    for i in range(len(o_dict)):
        o_dict.pop(i)


print(f'Удаление элемента из обычного словаря     = '
      f'{timeit("pop_ordinary()", globals=globals(), number=10000)}')
print(f'Удаление элемента из OrderedDict словаря  = '
      f'{timeit("pop_ordered()", globals=globals(), number=10000)}')


"""
Наполнение обычного словаря элементами    = 0.4349176000105217
Наполнение OrderedDict словаря элементами = 0.5779177000076743
Получение элемента из обычного словаря    = 0.44927179999649525
Получение элемента из OrderedDict словаря = 0.5202339000097709
Удаление элемента из обычного словаря     = 0.001310800003213808
Удаление элемента из OrderedDict словаря  = 0.0014239000011002645

Замеры однозначны - при использовании стандартных методов работы со-словарями
применять OrderedDict не имеет смысла.

Однако у OrderedDict есть несколько интересных методов внутренней  сортировки
элементов и удаления с концов словаря.
"""
