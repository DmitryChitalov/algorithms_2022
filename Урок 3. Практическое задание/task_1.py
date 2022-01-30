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
    def wrap(*args):
        start = time.time()
        res = func(*args)
        finish = time.time()
        print(f'Used time fo func {func}: {(finish - start)*1000}')
        return res
    return wrap


# O(n)
@time_checker
def add_to_list(n):
    lst = [i for i in range(n)]
    return lst


# O(n)
@time_checker
def add_to_dict(n):
    dict = {i: i**2 for i in range(n)}
    return dict

a = add_to_list(1000000)
b = add_to_dict(1000000)


# Изменение элементов
# O(n)
@time_checker
def insert_elem_list(list, el, pos):
    list.insert(pos, el)
    return list


# O(n)
@time_checker
def add_elem_dict(dict, el, pos):
    dict[pos] = el
    return dict


insert_elem_list(a, 22, 2)
add_elem_dict(b, 22, 2)


# Получение и удаление
@time_checker
def pop_elem_list(list, idx):
    el = list.pop(idx)
    return list


@time_checker
def pop_dict(dict, key):
    dict.pop(key)
    return dict

pop_elem_list(a, 1)
pop_dict(b, 1)


# Словарь заполняется медленнее, вероятно из-за хэширования и контроля уникальности ключей.
# Однако операции добавления, изменения и удаления элементов со словарем выполняются быстрее
# чем операции со списком, полагаюпо той же самой причине - хэширование