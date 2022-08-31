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

def time_of_function(func) :
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped
# b)
lst_1 = [2, 3, 4]
#
@time_of_function
def get_el(lst):
    for i in range(len(lst)): #O(n)
        print(lst[i])         #O(1)

get_el(lst_1)
#
#
dct_1 = {'a': 1, 'b': 2, 'c': 3}
@time_of_function
def get_el_2(dct):
    for key in dct.keys():  #O(n)
        print(dct[key])     #O(1)

get_el_2(dct_1)

#c)
# @time_of_function
# def pop_out(lst):  #O(n)
#     while lst:   #O(n)
#         print(lst.pop())  # O(1)
# pop_out(lst_1)
#
# @time_of_function
# def del_out(lst):  #O(n^2)
#     for i in range(len(lst)-1):  #O(n)
#         del lst[i]  # O(n)
# del_out(lst_1)
#







@time_of_function
def pop_out_2(dct):  #0(n)
    for key in list(dct): #O(n)
        print(dct.pop(key))   #O(1)
pop_out_2(dct_1)

@time_of_function    #O(n)
def del_out_2(dct):  #0(n)
    for key in list(dct):  # O(n)
        del dct[key]    #O(1)
del_out_2(dct_1)

di