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

from time import perf_counter


lst_obj1 = []
dict_obj1 = {}


def time_counter(func):
    def wrap(*args, **kwargs):
        t1 = perf_counter()
        func(*args, **kwargs)
        t2 = perf_counter()
        return print(t2 - t1, end='')
    return wrap

# Заполнение списка и словаря
####################################################################


@time_counter
def list_filling(lst_obj: list):
    for i in range(0, 1000):       # O(n)
        lst_obj.append(i)          # O(1)
    return lst_obj                 # O(n)


@time_counter
def add_el_to_list(lst_obj):
    lst_obj.append(1)              # O(1)


@time_counter
def dict_filling(dict_obj):
    for i in range(0, 1000):       # O(n)
        dict_obj.setdefault(i)     # O(1)
    return dict_obj                # O(n)


@time_counter
def add_el_to_dict(dict_obj):
    dict_obj.setdefault(1000)      # O(1)


print('заполнение списка и словаря')
list_filling(lst_obj1)
print(' лист цикл')
dict_filling(dict_obj1)    # наполнение словаря в цикле происходит медленнее
print(' словарь цикл')
add_el_to_list(lst_obj1)
print(' лист элемент')
add_el_to_dict(dict_obj1)  # добавление единичного елемента в словарь быстрее чем в список
print(' словарь элемент')


# Получение элемента списка и словаря
print('####################################################################')


@time_counter
def get_some_el_from_list(lst_obj):
    for i in lst_obj:                # O(n)
        continue                     # O(1)

@time_counter
def get_el_from_list(lst_obj):       # O(1)
    return lst_obj[0]                # O(1)

@time_counter
def get_some_el_from_dict(dict_obj):
    for i in dict_obj:               # O(n)
        continue                     # O(1)

@time_counter
def get_el_from_dict(dict_obj):      # O(1)
    return dict_obj[1]               # O(1)


print('получение элемента списка и словаря')
get_some_el_from_list(lst_obj1)
print(' лист цикл')
get_some_el_from_dict(dict_obj1)      # доступ к элементу словаря в цикле медленнее чем в списке
print(' словарь цикл')
get_el_from_list(lst_obj1)
print(' лист элемент')
get_el_from_dict(dict_obj1)           # доступ к одному элементу словаря быстрее чем в списке
print(' словарь элемент')
# удаление элемента списка и словаря
print('####################################################################')


@time_counter
def devastate_list(lst_obj):
    for i in range(0, 1000):       # O(n)
        lst_obj.pop()              # O(1)

@time_counter
def delete_el_from_list(lst_obj):
    lst_obj.pop()

@time_counter
def devastate_dict(dict_obj):
    for i in range(0, 1000):       # O(n)
        dict_obj.pop(i)            # O(1)

@time_counter
def delete_el_from_dict(dict_obj):
    dict_obj.pop(1000)


print('удаление элементов из списка и словаря')
devastate_list(lst_obj1)
print(' лист цикл')
devastate_dict(dict_obj1)
print(' словарь цикл')    # в цикле элементы словаря удаляются медленне
delete_el_from_list(lst_obj1)
print(' лист элемент')
delete_el_from_dict(dict_obj1)
print(' словарь элемент')  # удаление одного элемента в словаре происходит быстрее чем в списке

