"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
import cProfile

standart_dict = {}
ordered_dict = OrderedDict()
for_upd = [(i, i) for i in range(100)]


def filling_dct(dct):
    for i in range(10000):
        dct[i] = i
    return dct


def dict_pop(dct):
    for i in range(10000):
        dct.popitem()


def dict_update(dct, upd):
    for i in range(10000):
        dct.update(upd)


def main_1():
    filling_dct(standart_dict)
    filling_dct(ordered_dict)
    dict_pop(standart_dict)
    dict_pop(ordered_dict)
    dict_update(standart_dict, for_upd)
    dict_update(ordered_dict, for_upd)


cProfile.run('main_1()')

"""
Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.098    0.098 <string>:1(<module>)
        2    0.002    0.001    0.002    0.001 task_4.py:18(filling_dct)
        2    0.003    0.001    0.005    0.002 task_4.py:25(dict_pop)
        2    0.003    0.002    0.091    0.046 task_4.py:30(dict_update)
        1    0.000    0.000    0.098    0.098 task_4.py:35(main_1)
        1    0.000    0.000    0.098    0.098 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    10000    0.001    0.000    0.001    0.000 {method 'popitem' of 'collections.OrderedDict' objects}
    10000    0.001    0.000    0.001    0.000 {method 'popitem' of 'dict' objects}
    10000    0.070    0.000    0.070    0.000 {method 'update' of 'collections.OrderedDict' objects}
    10000    0.018    0.000    0.018    0.000 {method 'update' of 'dict' objects}
    
Вывод:
Операции наполнения и удаления идентичны как для dict, так и OrderedDict, 
но операции обновления гораздо быстрее у обычного словаря dict.
Это связанно с OrderedDict. Изначально он создавался для частых операций 
переупорядочивания.
Что касательно смысла использования OrderedDict в Python 3.6 и более поздних версиях.
Смысл есть. Так как при использовнии OrderedDict в коде, мы явно 
сообщаем, что нам важен порядок следования елементов и наш код на него 
операется и с ним взаимодействует.
"""