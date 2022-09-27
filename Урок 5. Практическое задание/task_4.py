"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import defaultdict

from timeit import timeit


regular_dict = {}
for i in range(100):
    regular_dict[i] = i + 1



def_dict = defaultdict(int)
for i in range(100):
    def_dict[i] = i + 1



def copy_dict(dictionary):
    return dictionary.copy()

print(timeit('copy_dict(regular_dict.copy())', globals=globals(), number=100))
print(timeit('copy_dict(def_dict.copy())', globals=globals(), number=100))

#0.00030017100000000185
#0.0014416599999999974

def dict_items(dictionary):
    return dictionary.items()

print(timeit('dict_items(regular_dict.copy())', globals=globals(), number=100))
print(timeit('dict_items(def_dict.copy())', globals=globals(), number=100))


#0.0001515850000000027
#0.0009232679999999979

def changing_dict(dictionary):
    for i in range(len(dictionary)):
        dictionary[i] = i + 10
    return dictionary

print(timeit('changing_dict(regular_dict.copy())', globals=globals(), number=100))
print(timeit('changing_dict(def_dict.copy())', globals=globals(), number=100))

#0.0010771580000000017
#0.0023695339999999995

"""
При операциях создания копии, получения пары значений ключ значение и изменения 
значений в словаре, обычный словарь работает быстрее чем defaultdict(), поэтому 
его использование для стандартных операций со словарем не имеет смысла.
"""