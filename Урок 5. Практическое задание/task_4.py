"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ord_dict = OrderedDict()

print(timeit("""for i in range(1000):
    my_dict[i] = i""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.0489085
print(timeit("""for i in range(1000):
    my_ord_dict[i] = i""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.065695
# Наполнение упорядоченного словаря происходит дольше, чем обычного

print(timeit("""for i in my_dict:
    my_dict[i] += 1""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.07001110000000002
print(timeit("""for i in my_ord_dict:
    my_ord_dict[i] += 1""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.0972634
# Изменение содержимого упорядоченного словаря происходит дольше, чем обычного

print(timeit("""for i in list(my_dict):
    my_dict.pop(i)""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.0007578000000000307
print(timeit("""for i in list(my_ord_dict):
    my_ord_dict.pop(i)""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.00029919999999999947
# А вот удаление удаление по ключу работает в упорядоченном словаре быстрее

for i in range(1000):
    my_dict[i] = i
for i in range(1000):
    my_ord_dict[i] = i

print(timeit("""for i in list(my_dict):
    my_dict.popitem()""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.0001870999999999956
print(timeit("""for i in list(my_ord_dict):
    my_ord_dict.popitem()""",  setup="from __main__ import my_dict, my_ord_dict", number=1000))
# 0.0002626000000000017
# Удаление методом popitem рабртает в упорядоченном словаре несколько медленнее

# В целом использование OrderedDict в Python 3.6+ не имеет особого смысла за исключением специфических задач, 
# когда порядок в словаре исключительно важен. 
# Например, польза от OrderedDict может быть при организации стеков и очередей, используя методы popitem и move_to_end
# с аргументом 'last'.
# Сравнение таких словарей учитывает в т.ч. порядок ключей.
