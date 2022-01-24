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
import time

""" (A) заполнение """
def time_measurement(func):
    """
    Function for measurement
    :arg: function arguments
    :return: function result
    """
    def wrapper(*args, **kwargs):
        print("Start measure")
        t_start = time.time()
        res = func(*args, **kwargs)
        t_stop = time.time()
        print("Function %s executed in %s seconds" % (func.__name__.title(), (t_stop - t_start)))
        return res
    return wrapper


"""Так как мы знаем количество итераций то сложность О(1)"""


@time_measurement
def array_filler(*args, **kwargs) -> list:
    """
    T(n) = O(1)
    :return: list
    """
    lst = []
    for i in range(1000):
        for j in range(10000):
            lst.append(i + j)                                   # O(1)
    # print("executed list slice...%s..." % lst[-50:-5:10])
    return lst


"""Так как мы знаем количество итераций то сложность О(1)"""


@time_measurement
def dict_filler(*args, **kwargs):
    """
    T(n) = O(1)
    :return: dict
    """
    my_dict = {}
    for i in range(1000):
        for j in range(10000):
            my_dict.update({i: i + j})                          # O(1)
    # print("executed dict slice ...{%s}..." % ", ".join((f"{i} : {k}" for i, k in list(my_dict.items())[-50:-5:10])))
    return my_dict


test_array = array_filler()  # Function Array_Filler executed in 0.9353170394897461 seconds
test_dict = dict_filler()  # Function Dict_Filler executed in 2.076969623565674 seconds

""" Однако время исполнения разное потому как для словаря вычисляется хеш, соответственно словать в 2 раза медленее """

""" (B) удаление """

@time_measurement
def remove_from_list(lst: list, index: int) -> list:
    """
    T(n) = O(1)
    :param lst: list
    :param index: int
    :return: list
    """
    try:
        lst.pop(index)                  # O(1)
    except IndexError:
        print("Index out of range")
    return lst

@time_measurement
def remove_from_dict(test_dict: dict, key) -> dict:
    """
    T(n) = O(1)
    :param test_dict: dict
    :param key:  valid key for dict, int or str
    :return: dict
    """
    try:
        del test_dict[key]              # O(1)
    except KeyError:
        print("Key is not valid")
    return test_dict


remove_from_list(test_array, 1)  # Function Remove_From_List executed in 0.005974769592285156 seconds
remove_from_dict(test_dict, 1)  # Function Remove_From_Dict executed in 0.0 seconds

""" Удаление элемента происходит быстрее в словаре нежели в списке """

""" (B) изменение """

@time_measurement
def list_changing(lst: list, index: int, value) -> list:
    """
    :param lst: list
    :param index:  int
    :param value: int, list, str, dict, tuple
    :return: lst
    """
    try:
        lst.insert(index, value)            # O(1)
        print("changed value =", lst[index-3:index+3])
    except IndexError:
        print("Index out of range")
    return lst


@time_measurement
def dict_changing(test_dict: dict, key, value) -> dict:
    """
    T(n) = O(1)
    :param test_dict: dict
    :param key:  valid key for dict, int or str
    :param value: int, list, str, dict, tuple
    :return: dict
    """
    try:
        test_dict[key] = value              # O(1)
        print("changed value =", test_dict[key])
    except KeyError:
        print("Key is not valid")
    return test_dict


list_changing(test_array, 5, "test value")  # Function List_Changing executed in 0.00800013542175293 seconds
dict_changing(test_dict, 5, "test value")  # Function Dict_Changing executed in 0.0 seconds


""" изменение элемента происходит быстрее в словаре нежели в листе 
    из этого следует что запись в словарь происходит дольше чем в списке, но операции изменений и удаление 
    быстрее чем в список"""