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

from time import time
from random import choice



def time_measurement(function):
    def wrapper(*args):
        start = time()
        function(*args)
        end = time()
        time_diff = end - start
        return time_diff

    return wrapper


my_list = []
my_dict = {}

# a)
@time_measurement
def measure_list(i):
    for i in range(i):
        my_list.append(choice(range(1, 1000000)))  # сложность операции O(1)
    return my_list


@time_measurement
def measure_dict(i):
    for i in range(i):
        my_dict[i] = (choice(range(1, 1000000)))  # сложность операции O(1)
    return my_dict


print(measure_list(1000000))
print(measure_dict(1000000))
print(len(my_list))
print(len(my_dict))

# Результаты замеров:
# Время выполнения функции measure_list - 0.12497186660766602
# Время выполнения функции measure_dict - 0.17216920852661133
# Cловарь заполняется дольше из-за необходимости вычисления хешей ключей




# b)
@time_measurement
def getting_list(i):
    for i in range(i):
        my_list[i] = my_list[i + 1]     # сложность операции O(1)
    return my_list

@time_measurement
def getting_dict(dct):
    for i in range(899999, 999999):
        dct[i] = 'fill'                 # сложность операции O(1)

print(getting_list(100000))
print(getting_dict(my_dict))

# Результаты замеров:
# Время выполнения функции getting_list - 0.015621662139892578
# Время выполнения функции getting_dict - 0.01563096046447754
# скорость операции получения произвольного (без поиска конкретного значения)
# элемента для списка (обращение к ячейки памяти по ее адресу)
# не больше, чем для словаря (обращение к нужному элементу по ключу)


# c)
@time_measurement
def remove_list(i):
    for i in range(i):
        my_list.pop(i)  # сложность операции O(n)
    return my_list


@time_measurement
def remove_dict(i):
    for i in range(i):
        my_dict.pop(i)  # сложность операции O(1)
    return my_dict


print(remove_list(10000))
print(remove_dict(10000))
print(len(my_list))
print(len(my_dict))

# Результаты замеров:
# Время выполнения функции remove_list - 9.92276930809021
# Время выполнения функции remove_dict - 0.015615463256835938
# Сложность удаления элементов списка O(n), в связи с этим скорость удаление элементов словаря (у него сложность O(1))
# происходит значительно быстрее чем списка.