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
from random import randint


def time_decorator(function):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        print(f'Время выполнения {function}: {perf_counter() - start}')
        return result
    return wrapper


# a - заполнение списка
@time_decorator
def list_fill(min_num, max_num):  # O(n)
    my_list = [randint(1, 100) for i in range(randint(min_num, max_num))]
    return my_list


# a - заполнение словаря
@time_decorator
def dict_fill(**kwargs):  # O(n)
    created_dict = dict((key, value) for key, value in kwargs.items())
    return created_dict


# b - выполните со списком и словарем операции: получения и удаления элемента


@time_decorator
def take_list_item(lst, idx):  # O(1)
    try:
        return print(f'Элемент с индексом {idx} = {lst[idx]}')
    except IndexError:
        return print('Out of range')


@time_decorator
def delete_item_from_lst(lst):  # O(1)
    return f'Удален элемент - {lst.pop()}'


@time_decorator
def take_from_dict(dict_name, key_name):  # O(1)
    try:
        return print({dict_name.get(key_name)})
    except ValueError:
        return print('Такого ключа нет')


@time_decorator
def delete_from_dict(dict_name, key_name):  # O(1)
    try:
        return print(f'Удалено из словаря: {dict_name.pop(key_name)}')
    except ValueError:
        return print('Такого ключа нет')


# Заполнение списка и словаря
print(list_fill(1, 100))
print(dict_fill(name='Ksenia', age='30', city='Kazan'))
# Получаем и удаляем эл-т из списка
example_list = list_fill(1, 10)
take_list_item(example_list, 2)
print(delete_item_from_lst(example_list))
# Получаем и удаляем эл-т из
example_dict = dict_fill(name='Ksenia', age='30', city='Kazan')
take_from_dict(example_dict, 'city')
delete_from_dict(example_dict, 'age')

"""
Вывод: Операции со словарем выполняются медленнее, чем со списком
"""