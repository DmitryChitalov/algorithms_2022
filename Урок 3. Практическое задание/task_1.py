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
from random import randint
from time import perf_counter


def time_counter(f):
    def wrapper(n):
        start = perf_counter()
        result = f(n)
        run_time = perf_counter() - start
        print(f'время выпполнения функции {f.__name__}: {run_time}.')
        return result
    return wrapper


# a) заполнение
@time_counter
def fill_list(array):               # общая O(N)
    lst = []                        # O(1)
    for el in array:                # O(N)
        lst.append(el)              # O(1)
    return lst                      # O(1)


@time_counter
def fill_dict(array):               # общая O(N)
    dct = {}                        # O(1)
    for j in range(len(array)):     # O(N)
        dct[j] = array[j]           # O(1)
    return dct                      # O(1)


# b) извлечение
@time_counter
def read_list(array):               # общая O(N)
    for j in range(len(array)):     # O(N)
        temp = array[i]             # O(1)


@time_counter
def read_dict(dct):                 # общая O(N)
    for key in dct:                 # O(N)
        temp = dct[key]             # O(1)


# c) удаление
@time_counter
def del_list(lst):                   # общая O(N^2)
    for j in range(len(lst)):        # O(N)
        lst.pop(0)                   # O(N)


@time_counter
def del_dict(dct):                   # общая O(N)
    for j in range(len(dct)):        # O(N)
        dct.pop(j)                   # O(1)


if __name__ == '__main__':
    m_len = int(input('Введите длину списка/словаря: '))
    temp_list = []
    for i in range(m_len):
        temp_list.append(randint(0, 100))

    # a) заполнение
    new_list = fill_list(temp_list)
    new_dict = fill_dict(temp_list)
    # Вывод: список заполняется быстрее, так как словарь это хэш-таблица и нужно считать хэш и разбираться с коллизиями

    # b) чтение
    read_list(new_list)
    read_dict(new_dict)
    # Вывод: чтение происходит примерно одинаково

    # с) удаление
    del_list(new_list)
    del_dict(new_dict)
    # Вывод: список очищается дольше, потому что при каждом удалении пересчитываются все индексы.
