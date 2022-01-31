"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: получения и удаления элемента.
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
from time import perf_counter


def time_measurement(func):
    def wrapper(*args):
        start = perf_counter()
        func(*args)
        finish = perf_counter()
        return f'\n{func.__name__}: {finish-start}'
    return wrapper


@time_measurement
def list_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive.append(i)  # O(1)


@time_measurement
def dict_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive[i] = i  # O(1)


just_list = []
just_dict = {}
print(list_filling(just_list, 10000))
print(dict_filling(just_dict, 10000))
print('Словарь заполняется медленнее, т.к. у словаря помимо заполнения происходит еще генерация хэша')


@time_measurement
def change_delete_list():  # O(n)
    for i in range(5000):  # O(1)
        just_list[i] = just_list[i+1]  # O(1)
    for i in range(5000):  # O(1)
        just_list.pop(i)  # O(n)


@time_measurement
def change_delete_dict():  # O(1)
    for i in range(5000):  # O(1)
        just_dict[i] = just_dict[i+1]  # O(1)
    for i in range(5000):  # O(1)
        just_dict.pop(i)  # O(1)


print(change_delete_list())
print(change_delete_dict())
print('Словарь изменяется быстрее, т.к. все операции проходят за время О(1)')
