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


def time_decor(func):
    def timer(*args):
        start = time.time()
        func(*args)
        end = time.time()
        time_val = end - start
        print(f'Time for {func.__name__} = {time_val}')
        return time_val
    return timer


# a)
new_list = []
new_dict = {}


# O(1)
@time_decor
def list_fill(val):
    for i in range(val):
        new_list.append(i)
    return new_list


# O(1)
@time_decor
def dict_fill(val):
    for i in range(val):
        new_dict[i] = i
    return new_dict


list_fill(100000)  # Time for list_fill = 0.0189974308013916
dict_fill(100000)  # Time for dict_fill = 0.026000261306762695
# Список заполняется быстрее
# | ---------------------------------------------------------- |
# b)


# O(n)
@time_decor
def list_update1():
    for i in new_list:
        new_list[i] = i + 1
    return new_list


# O(n)
@time_decor
def dict_update1():
    for i in new_dict:
        new_dict[i] = i + 1
    return new_dict


list_update1()  # Time for list_update = 0.00700068473815918
dict_update1()  # Time for dict_update = 0.020002126693725586
# Список изменяется быстрее


# O(1)
@time_decor
def list_remove(val):
    for i in range(val):
        del new_list[-1]
    return new_list


# O()
@time_decor
def dict_remove(val):
    for i in range(val):
        del new_dict[i]
    return new_dict


list_remove(100000)  # Time for list_remove = 0.008001089096069336
dict_remove(100000)  # Time for dict_remove = 0.02200150489807129
''' 
Список удаляет элементы быстрее.
Вывод: список быстрее во всём
'''
