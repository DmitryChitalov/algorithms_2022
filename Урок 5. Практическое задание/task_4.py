"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import repeat


# insert in dict
setup = """
from collections import OrderedDict
simple_dict = dict()
order_dict = OrderedDict()

def test_simple_dict_insert(n):
    for i in range(n):
        simple_dict[i] = i

def test_order_dict_insert(n):
    for i in range(n):
        order_dict[i] = i
"""
# 0.05475710006430745
print(f"{min(repeat(stmt='test_simple_dict_insert(10**5)', repeat=3, setup=setup, number=10))=}")
# 0.08110650000162423
print(f"{min(repeat(stmt='test_order_dict_insert(10**5)', repeat=3, setup=setup, number=10))=}")
# ===> simple_dict и order_dict вставляют значения за сопоставимое время, 
# но simple_dict немного быстрее. Характеризуются скоростью O(1)
print('=================================================================')

# get from dict
setup = """
from collections import OrderedDict
simple_dict = dict()
order_dict = OrderedDict()
simple_dict = {i:i for i in range(10**6)}
order_dict = OrderedDict({i:i for i in range(10**6)})

def test_simple_dict_get(n):
    for i in range(n):
        return simple_dict[i]

def test_order_dict_get(n):
    for i in range(n):
         return order_dict[i]
"""
# 9.399955160915852e-06
print(f"{min(repeat(stmt='test_simple_dict_get(10**5)', repeat=3, setup=setup, number=10))=}")
# 9.100069291889668e-06
print(f"{min(repeat(stmt='test_order_dict_get(10**5)', repeat=3, setup=setup, number=10))=}")
# ===> simple_dict и order_dict извлекают произвольные значения за сопоставимое время O(1)
print('=================================================================')


# popitem last
setup = """
from collections import OrderedDict
simple_dict = dict()
order_dict = OrderedDict()
simple_dict = {i:i for i in range(10**6)}
order_dict = OrderedDict({i:i for i in range(10**6)})

def test_simple_dict_popitem_last(n):
    for i in range(n):
        return simple_dict.popitem()

def test_order_dict_popitem_last(n):
    for i in range(n):
         return order_dict.popitem()
"""
# 1.3599987141788006e-05
print(f"{min(repeat(stmt='test_simple_dict_popitem_last(10**5)', repeat=3, setup=setup, number=10))=}")
# 1.2200092896819115e-05
print(f"{min(repeat(stmt='test_order_dict_popitem_last(10**5)', repeat=3, setup=setup, number=10))=}")
# ===> simple_dict и order_dict извлекают значения с конца за сопоставимое время O(1)
print('=================================================================')

# popitem first
setup = """
from collections import OrderedDict
simple_dict = {i:i for i in range(10**6)}
order_dict = OrderedDict(simple_dict)

def test_simple_dict_popitem_first(n):
    for i in range(n):
        return simple_dict.pop(i)

def test_order_dict_popitem_first(n):
    for i in range(n):
        return order_dict.popitem(False)
"""
# 7.70005863159895e-06
print(f"{min(repeat(stmt='test_simple_dict_popitem_first(10**5)', repeat=3, setup=setup, number=1))=}")
# 7.699942216277122e-06
print(f"{min(repeat(stmt='test_order_dict_popitem_first(10**5)', repeat=3, setup=setup, number=1))=}")
# ===> simple_dict и order_dict извлекают значения с начала за сопоставимое время O(1)
print('=================================================================')

# move_to_end
setup = """
from collections import OrderedDict
simple_dict = {i:i for i in range(10**6)}
order_dict = OrderedDict(simple_dict)

def test_simple_dict_move_to_end(n):
    for i in range(n):
        val = simple_dict[i]
        del simple_dict[i]
        simple_dict[len(simple_dict)] = val

def test_order_dict_move_to_end(n):
    for i in range(n):
        order_dict.move_to_end(i)
"""
# 0.0016388000221922994
print(f"{min(repeat(stmt='test_simple_dict_move_to_end(10**4)', repeat=3, setup=setup, number=1))=}")
# 0.0007449999684467912
print(f"{min(repeat(stmt='test_order_dict_move_to_end(10**4)', repeat=3, setup=setup, number=1))=}")
# ===> перемещение элементов в конец(начало) в order_dict немного быстрее чем в simple_dict
# скорость обоих операция характеризуется O(1)
print('=================================================================')

# С версии python 3.6 случаев для применения Orderdict стало меньше, его можно использовать в 3х случаях:
# 1-Хотим показать явно что порядок имеет значение
# 2-Хотим перемещать элементы в конец или начало, для этого есть удобные методы
# 3-Хотим сравнивать словари с учетом порядка