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

# a

import time


def my_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()
        print("После вызова функции.")

    return wrapper


def time_decor(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        ret = func(*args, **kwargs)
        time_end = time.time()
        print('Время выполнения функции %s =  %s' % (func.__name__, time_end - time_start))
        return ret

    return wrapper


@time_decor
def test_func():
    print('test func')


@time_decor
def fill_list(my_lst, my_data):  # o(n)
    for i in range(my_data):
        my_lst.append(i)
    return my_lst


@time_decor
def fill_dict(my_dict, my_data):  # o(n)
    for i in range(my_data):
        my_dict[i] = i
    return my_dict


if __name__ == '__main__':
    lst = []
    dct = {}
    lst = fill_list(lst, 1000000)
    dct = fill_dict(dct, 1000000)


# Несмотря на то что в О-нотации сложность одинаковая,  Список заполняется быстрее, потому что для него не нужно
# делать хэш-таблицу, как для словаря , но это заментно только на больших объемах данных ( у меня это где то от 8000
# элеметнтов и больше)


# b
@time_decor
def delete_elem_lst1(my_lst, elem):  # O(n)
    try:
        my_lst.remove(elem)
    except:
        print('Элемент отсутствует')
    return my_lst


@time_decor
def update_elem_lst1(my_lst, idxs, my_data):  # O(n) - что бы менять сразу несколько
    for i in idxs:
        my_lst[i] = my_data
    return my_lst


@time_decor
def delete_elem_dct(my_dct, elem_key):  # O(1)
    del my_dct[elem_key]

    return my_dct


@time_decor
def update_elem_dct(my_dct, elem_keys, my_data):  # O(n) - что бы менять сразу несколько
    for i in elem_keys:
        my_dct[i] = my_data

    return my_dct


ke = [i for i in range(1, 99989)]

update_elem_lst1(lst, ke, 145654)
update_elem_dct(dct, ke, 145654)

lst = delete_elem_lst1(lst, 99990)
dct = delete_elem_dct(dct, 99990)

# Удаление быстрее и проще в О-нотации в словаре , тк работать с хэш таблицей быстрее чем перебирать элементы в
# списке.
#
# изменение существующих элементов в словаре и списке (при обращению к нему по индексу ) примерно одинаковое
# но на больших значених получается, что изменение в списке быстрее (хотя возможно это потому что идет подряд)
