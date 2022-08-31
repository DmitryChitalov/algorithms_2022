"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit, default_timer


def add_to_dict_test():
    my_dict1 = {}
    for i in range(1000):
        my_dict1[i] = i + 1


def add_to_orddict_test():
    my_orddict1 = OrderedDict()
    for i in range(1000):
        my_orddict1[i] = i + 1


"""

Далее для технических целей тестирования функции popitem и других методов
создадим функции формирующие тестовые массивы данных 


"""


def fill_dict_test():
    my_dict2 = {}
    for i in range(1000):
        my_dict2[i] = i + 1
    return my_dict2


def fill_orddict_test():
    my_orddict2 = OrderedDict()
    for i in range(1000):
        my_orddict2[i] = i + 1
    return my_orddict2


def dict_pop_test(dict1):
    for i in range(len(dict1)):
        dict1.popitem()
        i += 1


def orddict_pop_test(orddict1):
    for i in range(len(orddict1)):
        orddict1.popitem(last=True)
        i += 1


new_dict = fill_dict_test()
new_orddict = fill_orddict_test()


def dict_move_to_start(dict2):
    dict21 = {list(dict2.items())[-1][0]: list(dict2.items())[-1][1]}

    dict2, dict21 = dict21, dict2
    dict2.update(dict21)


def orddict_move_to_start(orddict2):
    orddict2.move_to_end(list(orddict2)[-1], last=False)


print("________________Сравнение времени функции добавления элемента в словари________________________")
print(timeit("add_to_dict_test()", setup="from __main__ import add_to_dict_test",
             number=1000))
print(timeit("add_to_orddict_test()", setup="from __main__ import add_to_orddict_test",
             number=1000))

print("________________Сравнение времени функции popitem________________________")
start_time = default_timer()
dict_pop_test(new_dict)
print(default_timer() - start_time)
start_time1 = default_timer()
orddict_pop_test(new_orddict)
print(default_timer() - start_time1)

new_dict1 = fill_dict_test()
new_orddict1 = fill_orddict_test()

print("________________Сравнение времени функции movetostart________________________")
start_time2 = default_timer()
dict_move_to_start(new_dict1)
print(default_timer() - start_time2)
start_time3 = default_timer()
orddict_move_to_start(new_orddict1)
print(default_timer() - start_time3)

"""


Выводы:
добавление и удаление последних элементов в обычный словарь происходит быстрее чем в упорядоченный,
более быстро происходит в ordereddict перенос последнего элемента в начало в связи с наличием встроенного метода.
Поэтому (если только не требуется постоянных перемещений элементов (изменение их порядка)) в Python версиях 
позже 3.6. смысла в использовании Ordereddict нет, можно и нужно использовать обычные словари.



"""
