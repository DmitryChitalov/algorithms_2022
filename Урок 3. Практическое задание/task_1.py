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


def benchmark(func):
    """
    Декоратор для замера времени
    :param func:
    :return:
    """
    import time

    def wrapper(*arg):
        start = time.time_ns()
        func(*arg)
        end = time.time_ns()
        print('[*] Время выполнения {}: {} наносекунд.'.format(func, end - start))

    return wrapper


# a)

@benchmark
def list_creation():
    list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # O(N)
    return list_1


@benchmark
def dict_creation():
    dict_1 = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
              6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
              11: 11, 12: 12, 13: 13, 14: 14, 15: 15,
              16: 16, 17: 17, 18: 18, 19: 19, 20: 20}  # O(N)
    return dict_1


list_creation()
dict_creation()

# Создание словаря занимает больше времени чем создание списка,
# т.к. создается не только элемент но и ключ


# b)

list_1 = [x for x in range(1000)]

dict_1 = {x: x for x in range(1000)}


@benchmark
def list_change_elem(list_1):
    list_1[999] = 'Blue'
    return list_1


@benchmark
def list_del_elem(list_1):
    list_1.pop(999)
    return list_1


@benchmark
def dict_change_elem(dict_1):
    dict_1[999] = 'Blue'
    return dict_1


@benchmark
def dict_del_elem(dict_1):
    dict_1.pop(999)
    return dict_1


list_change_elem(list_1)
dict_change_elem(dict_1)

list_del_elem(list_1)
dict_del_elem(dict_1)


# Модификация и удаление элемента в словаре быстрее чем списка
# Так как поиск по ключу происходит быстрее