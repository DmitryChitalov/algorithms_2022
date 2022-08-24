"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time


def time_measurement(func):
    def wrapper(*args):
        start = time.time()
        start_func = func(*args)
        end = time.time()
        result_time = end - start
        print(f'{func} время выполнения {result_time}')
        return start_func
    return wrapper


# Блок А - заполнение
print('Блок A')


@time_measurement
def add_list(n):
    """
    Функция для заполнения списка
    Алгоритм: простой генератор списка
    Сложность: O(n)
    """
    obj_list = [i for i in range(n)]  # O(n)
    return obj_list


@time_measurement
def add_list_2(n):
    """
    Функция для заполнения списка
    Алгоритм: цикл списка
    Сложность: O(n)
    """
    obj_list = []
    for i in range(n):  # O(n)
        obj_list.append(i)  # O(1)
    return obj_list


@time_measurement
def add_dict(n):
    """
     Функция для заполнения списка
     Алгоритм: простой генератор списка
     Сложность: O(n)
     """
    obj_dict = {x: x for x in range(n)}  # O(n)
    return obj_dict


@time_measurement
def add_dict_2(n):
    """
     Функция для заполнения списка
     Алгоритм: простой генератор списка
     Сложность: O(n)
     """
    obj_dict = {}
    for i in range(n):  # O(n)
        obj_dict[i] = i
    return obj_dict


add_list(10000000)
add_list_2(10000000)
add_dict(10000000)
add_dict_2(10000000)
"""
Быстрее заполняется список, веротяно всего, ключи у словарей хешируются и на это уходит больше времени

Блок A
<function add_list at 0x000001AA957BCB80> время выполнения 3.575593948364258
<function add_list_2 at 0x000001AA957C3160> время выполнения 5.573655843734741
<function add_dict at 0x000001AA957C3280> время выполнения 6.753004550933838
<function add_dict_2 at 0x000001AA957C33A0> время выполнения 7.18609094619751
"""

# Блок B - получение
print('Блок B')


@time_measurement
def get_list_item(obj_list):  # O(n)
    for i in obj_list:
        item = i


@time_measurement
def get_dict_item(obj_dict):
    for k in obj_dict.keys():  # O(n)
        item = k


obj_list = [i for i in range(100000)]
obj_dict = {x: x for x in range(100000)}
get_list_item(obj_list)
get_dict_item(obj_dict)


"""
На более больших данных, выигрывает словарь, опять же, из-за хешей

Блок B
<function get_list_item at 0x0000028BC61234C0> время выполнения 0.10471463203430176
<function get_dict_item at 0x0000028BC61235E0> время выполнения 0.1234135627746582
"""

# Блок С - извлечение
print('Блок C')


@time_measurement
def del_list_item(obj_list):
    """
    Сложность: O(n**2) 
    """
    for i in range(len(obj_list)):  # O(n)
        obj_list.pop()  # O(n)


@time_measurement
def del_list_item_2(obj_list):
    obj_list.remove(99999)  # O(n)


@time_measurement
def del_dict_items(obj_dict):
    copy_dict = obj_dict.copy()
    for k in obj_dict.keys():  # O(n)
        copy_dict.pop(k)  # O(1)


@time_measurement
def del_dict_items_2(obj_dict):
    del obj_dict[99999]  # O(1)


del_list_item_2(obj_list)
del_dict_items_2(obj_dict)
del_list_item(obj_list)
del_dict_items(obj_dict)


"""
При удалении методом pop() через цикл, список быстрее удаляет, хотя сложность квадратичная 
Метод del работает быстрее в словаре, потому что в словарях сложность константная, а в списках линейная, все зависит от положения удаляемого элемента

Блок C
<function del_list_item_2 at 0x000001DC12403820> время выполнения 0.0029675960540771484
<function del_dict_items_2 at 0x000001DC12403A60> время выполнения 0.0
<function del_list_item at 0x000001DC12403700> время выполнения 0.005033254623413086
<function del_dict_items at 0x000001DC12403940> время выполнения 0.007964849472045898
"""
