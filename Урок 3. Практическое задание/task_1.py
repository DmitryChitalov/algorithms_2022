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

def time_of_func(func):
    import time

    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        func(*args, **kwargs)
        print(f'Время выполнения функции {func.__name__} равно {time.perf_counter() - t}')
    return wrapper


@time_of_func                               #> 0.0009686
def fill_list(n, new_list):
    for i in range(n):
        new_list.append(i)                  #O(1)
    return new_list


my_list = []
fill_list(10000, my_list)


@time_of_func                               #> 0.0013688999999999993
def fill_dict(n, new_dict):
    for i in range(n):
        new_dict[i] = i+1                   #O(1)
    return new_dict


my_dict = {}
fill_dict(10000, my_dict)

# заполнение списка быстрее, т.к. при заполнении словоря тратится  время на хэширование
@time_of_func                               #> 0.006703600000000004
def change_list(n, new_list):
    for i in range(n):
        new_list.insert(i, i + 1)           #O(n)
    return new_list


print(change_list(1000, my_list))


@time_of_func                               #> 0.00011830000000000174
def change_dict(n, new_dict):
    for i in range(n):
        new_dict[i] = i + 1                 #O(1)
    return new_dict


print(change_dict(1000, my_dict))


@time_of_func                               #> 0.0017938999999999941
def remove_list_el(n, new_list):
    for i in range(n):
        new_list.pop(i)                     #O(n)
    return new_list


print(remove_list_el(1000, my_list))


@time_of_func                                #> 0.0001212999999999978
def remove_dict_el(n, new_dict):
    for i in range(n):
        new_dict.pop(i)                      #O(1)
    return new_dict


print(remove_dict_el(1000, my_dict))

# Изменение и удаление элементов словаря быстрее, чем изменение и удаление элементов списка.