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


def time_checker(func):
    def wrap(n):
        start = time.time()
        res = func(n)
        finish = time.time()
        print(f'Used time fo func {func}: {finish - start}')
        return res
    return wrap


@time_checker
def add_to_list(n):
    lst = [i for i in range(n)]
    return lst


@time_checker
def add_to_dict(n):
    dict = {i: i**2 for i in range(n)}
    return dict


a = add_to_list(50000)
b = add_to_dict(50000)

# Словарь заполняется медленнее, вероятно из-за хэширования и контроля уникальности ключей

@time_checker
def append_to_list(n):
    list = []
    for i in range(n):
        list.append(i)
    return list


c = append_to_list(50000)

@time_checker
def append_to_dict(n):
    dict = {}
    for i in range(n):
        dict[i] = i ** 2
    return dict

c = append_to_dict(50000)