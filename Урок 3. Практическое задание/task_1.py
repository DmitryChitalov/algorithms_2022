"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
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

def stopwatch(func):
    def wrapper(args=None):
        start = time.time()
        obj = func(args)
        end = time.time()
        print(f"Время операции {func} - {end - start} сек")
        return obj

    return wrapper


# а) заполнение списка и словаря
@stopwatch
def list_complation(*args):
    lst = [i for i in range(10 ** 7)]
    return lst


@stopwatch
def dict_complation(*args):
    dict = {i: i for i in range(10 ** 7)}
    return dict


# b) получение элемента списка и словаря

@stopwatch
def take_el_from_list(lst):
    return lst[9999998]


@stopwatch
def take_el_from_dict(dc):
    return dc[9999999]


# c) удаление элемента списка и словаря

@stopwatch
def delete_el_from_list(lst: list):
    lst.pop(9999999)
    return lst


@stopwatch
def delete_el_from_dict(dc: dict):
    dc.pop(9999999)
    return dc


test_lst = list_complation()
test_dict = dict_complation()

take_el_from_list(test_lst)
take_el_from_dict(test_dict)

test_lst = delete_el_from_list(test_lst)
test_dict = delete_el_from_dict(test_dict)
