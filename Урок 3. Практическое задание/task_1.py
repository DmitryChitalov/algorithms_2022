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

# Функция декоратор для замера времени
import time


def result_time(func):
    def user_func(*args):
        start = time.perf_counter()
        result = func(*args)
        print(time.perf_counter() - start)
        return result

    return user_func


# Задание а)
@result_time
def create_list(n):  # O(n)
    return [el for el in range(n)]


@result_time
def create_dict(n):  # O(n)
    return {el: el for el in range(n)}


"""
при одинаковой сложности список заполняется быстрее 
потому что при создании словаря считается хэш для ключей
"""


# Задание b)
@result_time
def get_list_item(user_list, n):  # O(1)
    return user_list[n]


@result_time
def get_dict_value(user_dict, key):  # O(1)
    return user_dict[key]


"""
при одинаковой сложности получение элемента словаря
происходит быстрее чем элемента списка, благодаря тому 
что ключ словаря это хэшируемый объект 
"""


# Задание c)
@result_time
def del_list_item(user_list, n):  # O(1)
    user_list.pop(n)
    return user_list


@result_time
def del_dict_value(user_dict, key):  # O(1)
    user_dict.pop(key)
    return user_dict


"""
при одинаковой сложности удаление элемента словаря
происходит быстрее чем элемента списка, благодаря тому 
что ключ словаря это хэшируемый объект 
"""

if __name__ == '__main__':
    # Задание а)
    my_list = create_list(1000)
    print(my_list)
    my_dict = create_dict(1000)
    print(my_dict)

    # Задание b)
    my_list_item = get_list_item(my_list, 500)
    print(my_list_item)
    my_dict_value = get_dict_value(my_dict, 500)
    print(my_dict_value)

    # Задание c)
    my_list = del_list_item(my_list, 500)
    print(my_list)
    my_dict = del_dict_value(my_dict, 500)
    print(my_dict)
