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


def calc_time(func):
    def user_func(*args):
        start = time.perf_counter()
        result = func(*args)
        print(time.perf_counter() - start)
        return result

    return user_func


# task a
@calc_time
def create_list(n):  # O(n)
    return [el for el in range(n)]


@calc_time
def create_dict(n):  # O(n)
    return {el: el for el in range(n)}

# task b
@calc_time
def get_val_from_list(user_list, n):  # O(1)
    return user_list[n]


@calc_time
def get_val_from_dict(user_dict, key):  # O(1)
    return user_dict[key]

# task c
@calc_time
def del_from_list(user_list, n):  # O(1)
    user_list.pop(n)
    return user_list


@calc_time
def del_from_dict(user_dict, key):  # O(1)
    user_dict.pop(key)
    return user_dict


if __name__ == '__main__':
    # task a
    my_list = create_list(500)
    print(my_list)
    my_dict = create_dict(500)
    print(my_dict)
    # словарь медленнее, т.к. для него используется хэширование ключей

    # task b
    my_list_item = get_val_from_list(my_list, 100)
    print(my_list_item)
    my_dict_value = get_val_from_dict(my_dict, 100)
    print(my_dict_value)
    # словарь быстрее, т.к. используется хэш ключа

    # task c
    my_list = del_from_list(my_list, 100)
    print(my_list)
    my_dict = del_from_dict(my_dict, 100)
    print(my_dict)
    # словарь быстрее, т.к. используется хэш ключа