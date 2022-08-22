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


def time_func(func):  # декоратор для замера времени функции
    def result(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print(time.perf_counter_ns() - start_time)
        return res

    return result


# a) я понял задание так, что функция заполнения списка это когда мы в функцию передаем какой-то объект (например
# строку), функция создает список


@time_func
def make_list(obj):  # O(1) + O(1) + O(1)
    name_list = []
    for i in obj:  # O(1) - зависит от obj
        name_list.append(i)  # O(1)
    return name_list  # O(1)


@time_func
def make_dict(obj):  # O(n)
    return {x: x for x in obj}


print(make_list('abcde'))
print(make_dict('abcde'))

# b)
my_list = make_list('abcde')
my_dict = make_dict('abcde')


@time_func
def get_el_list(some_list, el):
    for i in some_list:  # O(n)
        if i == el:
            return i


@time_func
def get_el_dict(some_dict, el):
    for i in some_dict:  # O(n)
        if i == el:
            return some_dict[i]


print(get_el_list(my_list, 'a'))
print(get_el_dict(my_dict, 'a'))


# c)
@time_func
def del_el_list(some_list, el):  # O(n)
    for i in some_list:
        if i == el:
            some_list.remove(i)


del_el_list(my_list, 'a')
print(my_list)


@time_func
def del_el_dict(some_dict, el):  # O(n)
    for i in list(some_dict):
        if i == el:
            del some_dict[i]
    return some_dict


del_el_dict(my_dict, 'a')
print(my_dict)
