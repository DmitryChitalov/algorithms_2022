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
# a
from time import time


def func_speed(func):
    def s(*arg, **kwargs):
        start = time()
        answ = func(*arg, **kwargs)
        return answ, (time() - start)

    return s


@func_speed
def add_list(num):
    new_list = []
    for el in num:
        new_list.append(el)  # O(1)
    return new_list


@func_speed
def add_dict(num):
    new_dict = {}
    for el in num:
        new_dict[el] = el  # O(1)
    return new_dict


a = [num for num in range(1, 100001)]
answ_dict = add_dict(a)
answ_list = add_list(a)
print(answ_dict[1])
print(answ_list[1])


# При сравнении сложности между списком и словарем, сложность получается одинаковая, но при замерах времени словарь оказывается быстрее.
# update - словарь не бывает быстрее при таком написании кода, в среднем одинаковое время,
# a 2
def func_speed2(func):
    def s(*arg, **kwargs):
        start = time()
        answ = func(*arg, **kwargs)
        print((time() - start))
        return answ

    return s


@func_speed2
def add_list2(new_list, num):
    for el in num:
        new_list.append(el)  # O(1)
    return new_list


@func_speed2
def add_dict2(new_dict, num):
    for el in num:
        new_dict[el] = el  # O(1)
    return new_dict


a = [num for num in range(1, 100001)]
my_dict = {}
my_list = []
add_dict2(my_dict, a)
add_list2(my_list, a)


# a2 по примеру разбора дз показывает, что список быстрее

# b) получение элемента списка, оцените сложность в O-нотации
#    получение элемента словаря, оцените сложность в O-нотации
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени
@func_speed
def take_el_dict(my_dict):
    for i in range(1, 100001):
        element = my_dict[i]  # O(1)
    return 'done'


@func_speed
def take_el_list(my_list):
    for i in range(0, 100000):
        element = my_list[i]  # O(1)
    return 'done'


print('b_dict', take_el_dict(answ_dict[0]))
print('b_list', take_el_list(answ_list[0]))


# При одинаковых сложностях функций список оказывается быстрее

# с) удаление элемента списка, оцените сложность в O-нотации
#    удаление элемента словаря, оцените сложность в O-нотации
#    сделайте аналитику, что заполняется быстрее и почему
#    сделайте замеры времени

@func_speed
def del_el_dict(my_dict):
    for i in range(1, 100001):
        my_dict.pop(i) #O(1)
    return 'done'


@func_speed
def del_el_list(my_list):
    for i in range(10000):
        my_list.pop(i) #O(n)
    return 'done'


print('c_dict', del_el_dict(answ_dict[0]))
print('c_list', del_el_list(answ_list[0]))

#Тут все соответствует сложности, как и ожидалось словарь быстрее.