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


def time_measure(func):
    def wrapper():
        start = time()
        func()
        stop = time()
        time_delta = stop - start
        return time_delta, func()

    return wrapper


@time_measure
def fill_in_lst():  # общая сложность O(1)
    lst = []  # O(1)
    for el in range(1000000):  # O(1)
        lst.append(el)  # O(1)
    return lst  # O(1)


@time_measure
def fill_in_dct():  # общая сложность O(1)
    dct = {}  # O(1)
    for key in range(1000000):  # O(1)
        dct.setdefault(key)  # O(1)
    return dct  # O(1)


@time_measure
def change_in_lst():  # общая сложность O(1)
    lst = fill_in_lst()[1]  # O(1)
    for i in range(100):  # O(1)
        lst[i] = None  # O(1)
    return lst  # O(1)


@time_measure
def change_in_dct():  # O(1)
    dct = fill_in_dct()[1]  # O(1)
    for i in range(100):  # O(1)
        dct[i] = 'Not None'  # O(1)
    return dct  # O(1)


@time_measure
def del_in_lst():  # O(n)
    lst = fill_in_lst()[1]  # O(1)
    for i in range(100):  # O(1)
        del lst[i]  # O(n)
    return lst  # O(1)


@time_measure
def del_in_dct():  # O(n)
    dct = fill_in_dct()[1]  # O(1)
    for i in range(100):  # O(1)
        del dct[i]  # O(1)
    return dct  # O(1)


if __name__ == '__main__':
    from time import time

    # поскольку словарь создает (изменяет) хеш-таблицу,
    # время на наполнение, изменение записей в словаре затрачивается немного больше,
    # чем в списке, а операции удаления осуществляются быстрее в словаре
    # (в списке после удаления происходит еще смещение элементов).
    print(f'Разница во времени операций словаря и списка:\n'
          f'наполнения млн записей - {fill_in_dct()[0] - fill_in_lst()[0]}\n'
          f'изменения ста записей - {change_in_dct()[0] - change_in_lst()[0]}\n'
          f'удаления ста записей - {del_in_dct()[0] - del_in_lst()[0]}')
