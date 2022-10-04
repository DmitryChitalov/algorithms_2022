"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

    Comment:
    Fill List, duration (ns) = 388500
    Fill Dict, duration (ns) = 650400
    Listing результатов выполнения приложен после кода программы ниже.
    Словарь заполняется медленнее O(N) чем список O(N), потому что при заполнении словаря
    также заполняется hash - таблица ключей, для оптимизации последующих действий со словарем.

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

       Comment:
    Get from list, duration (ns) = 196900
    Get from dict, duration (ns) = 1500
    Listing результатов выполнения приложен после кода программы ниже.
    выборка элемента из словаря O(N) производится быстрее чем выборка элемента из списка O(N)  благодаря
    ранее  заполненной  hash - таблица ключей в словаре для оптимизации последующих действий со словарем.

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

          Comment:
    Del from list, duration (ns) = 78516200
    Del from dict, duration (ns) = 427500
    Listing результатов выполнения приложен после кода программы ниже.
    Удаление элемента из словаря O(N) производится намного быстрее
    чем удаление элемента из списка O(N^2)  благодаря
    ранее  заполненной  hash - таблица ключей в словаре для оптимизации последующих действий со словарем.


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped


@time_of_function
def fill_list():                            # O(N)
    result = []                             # O(1)
    for i in range(1, 10000):               # O(N)
        result.append(i)                    # O(1)
    return result                           # O(1)


@time_of_function
def fill_dict():                            # O(N)
    result = {}                             # O(1)
    for i in range(1, 10000):               # O(N)
        result[i] = i + 2                   # O(1)
    # print(result)
    return result                           # O(1)

@time_of_function
def get_from_list(input_lst):               # O(N)
    for i in range(1, len(input_lst) - 1):  # O(N)
        a = input_lst[i]                    # O(1)
    # print(result)
    return

@time_of_function
def get_from_dict(input_dict):                  # O(N)
    for i in (1, len(input_dict) - 1):          # O(N)
        a = input_dict[i]                       # O(1)
    # print(result)
    return                                      # O(1)


@time_of_function
def del_from_list(input_lst):                   # O(N^2)
    for i in input_lst:                         # O(N)
        del input_lst[0]                        # O(N)
    return

@time_of_function
def del_from_dict(input_dict):                  # O(N)
    key_lst  = list(input_dict)                 # O(N)
    for i in key_lst:                           # O(N)
       del input_dict[i]                        # O(1)
    return


if __name__ == '__main__':
    print(f'\n -- Timing of operations -- ')
    print(f'Fill List, duration (ns) = ', end="")
    lst1 = fill_list()
    print(f'Fill Dict, duration (ns) = ', end="")
    dict1 = fill_dict()

    print(f'')
    print(f'Get from list, duration (ns) = ', end="")
    get_from_list(lst1)
    print(f'Get from dict, duration (ns) = ', end="")
    get_from_dict(dict1)

    print(f'')
    print(f'Del from list, duration (ns) = ', end="")
    del_from_list(lst1)
    print(f'Del from dict, duration (ns) = ', end="")
    del_from_dict(dict1)


# Script listing:
#
#  -- Timing of operations --
# Fill List, duration (ns) = 388500
# Fill Dict, duration (ns) = 650400
#
# Get from list, duration (ns) = 196900
# Get from dict, duration (ns) = 1500
#
# Del from list, duration (ns) = 78516200
# Del from dict, duration (ns) = 427500
#
# Process finished with exit code 0

