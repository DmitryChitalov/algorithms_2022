"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


common_dict = {}
od_dict = OrderedDict()

print('Добавление элементов')
print(timeit("""for i in range(10):
                    common_dict[i]=i""", globals=globals(), number=100000))     # 0.15785196900014853
print(timeit("""for i in range(10):
                    od_dict[i]=i""", globals=globals(), number=100000))         # 0.13760679600000003

print('Чтение')
print(timeit("""for i in range(10):
                    common_dict[i]""", globals=globals(), number=100000))       # 0.16197109499989892
print(timeit("""for i in range(10):
                    od_dict[i]""", globals=globals(), number=100000))           # 0.13693380299991986

print('Сравнение словарей')
print(timeit('common_dict == common_dict', globals=globals(), number=100000))   # 0.03138516100079869
print(timeit('od_dict == od_dict', globals=globals(), number=100000))           # 0.03739172699988558

"""
По результатам замеров особой разицы между "стандартным" словарем и OrderedDict
нет. При этом, после версии 3.6 словари по умолчанию стали упорядоченными и, как
следствие необходимости в OrderedDict нет. Также стандартные словари удобнее в
сравнении - не надо думать о порядке. Но если порядок расположения элементов
словаря критически важен при сравнении, то без OrderedDict не обойтись.
"""
