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


def check_time(in_func):
    def time_counter(*args, **kwargs):
        start = time.perf_counter()
        result = in_func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Время работы функции {in_func.__name__} составило {end_time-start:.6f} секунд')
        return result
    return time_counter


"""Реализация первого задания"""


@check_time
def filling_list(end_num):
    out_list = [x for x in range(1, end_num)]
    return out_list


@check_time
def filling_dict(end_num):
    out_dict = dict((str(x), x) for x in range(1, end_num))
    return out_dict


print('Реализация первого задания')
out_list = filling_list(10000000)
out_dict = filling_dict(10000000)
#print(out_list)
#print(out_dict)


"""Реализация второго задания"""

@check_time
def get_list_elem(list_n, index):
    return list_n[index]


@check_time
def get_dict_elem(dict_n, key):
    return dict_n[key]


print('Реализация второго задания')

print(get_list_elem(out_list, 50000))
print(get_dict_elem(out_dict, '50000'))


print('Реализация третьего задания')
@check_time
def del_list_elem(list_n: list, pattern):
    list_n.remove(pattern)

@check_time
def del_dict_elem(dict_n: list, pattern):
    dict_n.pop(pattern)

del_list_elem(out_list, 50000)
del_dict_elem(out_dict, '50000')
