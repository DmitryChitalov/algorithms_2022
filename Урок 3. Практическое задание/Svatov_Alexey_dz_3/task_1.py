"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from random import randint
from time import time


def sw_decorator(func):
    def stopwatch(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} = {end - start}')
        return result

    return stopwatch


# --------------------------------------------------------a-------------------------------------------------------------

@sw_decorator
def fill_list(target_list, count_elems):
    for i in range(count_elems):  # O(n)
        target_list.append(randint(0, 1000))  # O(1) - для списка
    return target_list


@sw_decorator
def fill_dict(target_dict, count_elems):
    for i in range(count_elems):  # O(n)
        target_dict[i] = randint(0, 1000)  # O(1) - для словаря
    return target_dict


test_list = []
fill_list(test_list, 10000)  # время = 0.02413320541381836

test_dict = {}
fill_dict(test_dict, 10000)  # время = 0.02263951301574707

"""
Время выполнения каждой из функций сопоставимо, т.к. O big идентичны. 

В случае со списком добавление элемента происходит в конец списка, что не требует сдвига последующих элементов и 
последующего "пересчёта индексов" элементов, находящихся после места вставки.

В случае со словарём вставка происходит по принципу работы с хэш-таблицами, то есть по обращению к  "уникальному" ключу
"""


# --------------------------------------------------------b-------------------------------------------------------------

@sw_decorator
def change_list_elem(target_list, elem, new_value):
    target_list[elem] = new_value  # O(1)
    return target_list


@sw_decorator
def remove_list_elem(target_list, target_value):
    target_list.remove(target_value)  # O(n)
    return target_list


@sw_decorator
def pop_list_elem(target_list, elem):
    target_list.pop(elem)  # O(n)
    return target_list


@sw_decorator
def pop_list_not_elem(target_list):
    target_list.pop()  # O(1)
    return target_list


@sw_decorator
def change_dict_elem(target_dict, elem, new_value):
    target_dict[elem] = new_value  # O(1)
    return target_dict


@sw_decorator
def pop_dict_elem(target_dict, target_key):
    target_dict.pop(target_key)  # O(1)
    return target_dict


@sw_decorator
def popitem_dict_elem(target_dict):
    target_dict.popitem()  # O(1)
    return target_dict


change_list_elem(test_list, 50, 'test_new_value')  # время = 3.337860107421875e-06
change_dict_elem(test_dict, 50, 'test_new_value')  # время = 1.430511474609375e-06
remove_list_elem(test_list, 'test_new_value')  # 1.049041748046875e-05
pop_list_elem(test_list, 51)  # время = 3.5762786865234375e-06
pop_dict_elem(test_dict, 50)  # время = 1.6689300537109375e-06
pop_list_not_elem(test_list)  # время = 9.5367431640625e-07
popitem_dict_elem(test_dict)  # время = 1.430511474609375e-06

"""

При внесении изменений при работе со словарём скорость оказалась выше, хотя O big в случае словаря и списка идентичны.

Удаление из списка "по значению" оказалось наименее эффективным, как по времени, так и по о-нотации.

Удаление из списка по индексу менее эффективно, чем удаление из словаря по ключу, как с точки зрения O big, 
так и с точки зрения времени. 
Причина: "сдвиг" последующих элементов списка и необходимость "пересчёта" индексов.

Удаление последнего элемента списка и элемента словаря по принципу LIFO идентичны по о-нотации, 
но работа со списком оказалась быстрее.

"""
