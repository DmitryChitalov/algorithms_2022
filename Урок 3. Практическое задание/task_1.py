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

import time


def load_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'Время выполнения: {(time.perf_counter() - start)}')
        return result

    return wrapper


@load_time
def list_gen(n):  # Сложность O(n)
    return [i for i in range(1, n + 1)]


@load_time
def dct_gen(n):  # Сложность O(n)
    return {i: '1' for i in range(1, n + 1)}


print(list_gen(100))
print(dct_gen(100))


# Вывод: так как при создании словаря хэшируются ключи, то их заполнение происходит медленнее.

@load_time
def elm_of_list(n, lst):  # O(n)
    res = [i for i in lst if i == n]
    return res


@load_time
def elm_of_dict(n, dct):  # O(n)
    return dct[n]


print(elm_of_list(1, [1, 2, 3, 7, 0]))
print(elm_of_dict(1, {1: '2', 3: 'u', 0: 'p'}))


#  Вывод: из словаря получить значение быстрее, чем из списка, так как извлечение работает по ключу.

@load_time
def pop_out_lst(item, lst):  # O(n)
    lst.remove(item)
    return lst


@load_time
def pop_out_dct(item, dct):  # O(1)
    del dct[item]
    return dct


print(pop_out_lst(1, [1, 2, 3, 7, 0]))
print(pop_out_dct(1, {1: '2', 3: 'u', 0: 'p'}))

# Вывод: удаление из словаря происходит быстрее. Причина - все те-же ключи )

