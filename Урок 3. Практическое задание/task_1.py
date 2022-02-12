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


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        delta_time = time.time() - start_time
        print(f"{func.__name__} Время выполнения {delta_time}")
        return result
    return wrapper


@execution_time
def filling_list(element_count):
    elements_list = [2 * i for i in range(element_count)]  # O(n)
    return elements_list  # O(1)


@execution_time
def filling_dict(element_count):
    elements_dict = {i: 2 * i for i in range(element_count)}  # O(n)
    return elements_dict  # O(1)


@execution_time
def update_list(change_list):
    for ind in range(len(change_list)):  # O(n)
        change_list[ind] += 4  # O(1)
    return


@execution_time
def update_dict(change_dict):
    for key in change_dict:  # O(n)
        change_dict[key] += 4  # O(1)
    return


@execution_time
def clear_list(fill_list):
    for _ in range(len(fill_list)):  # O(n)
        # del fill_list[0]  # O(n) результирующая сложность O(n^2)
        fill_list.pop()  # O(1) результирующая сложность O(n)


@execution_time
def clear_dict(fill_dict):
    for key in list(fill_dict.keys()):  # O(n)
        del fill_dict[key]  # O(1)


count = 10000000

list_obj = filling_list(count)
dict_obj = filling_dict(count)

update_list(list_obj)
update_dict(dict_obj)

clear_list(list_obj)
clear_dict(dict_obj)


"""
Один из результатов работы (соотношение сохраняется при повторных запусках):
filling_list Время выполнения 0.6582129001617432
filling_dict Время выполнения 1.0910818576812744
update_list Время выполнения 0.7540090084075928
update_dict Время выполнения 0.9694085121154785
clear_list Время выполнения 0.5984015464782715
clear_dict Время выполнения 0.6382606029510498


Заполнение словаря происходит медленне списка, т. к. происходит хэширование ключей словаря.
Не могу объяснить скорость выполнения изменений/удалений значений списка и словаря, т. к. в словаре
доступ по ключу должен быть быстрее, иначе для чего делать хеширование?
Удаление/добавление элемента не из/в конец списка имеет квадратичную сложность, т. к. происходит сдвиг элементов
относительно удаляемого/вставляемого.  
"""