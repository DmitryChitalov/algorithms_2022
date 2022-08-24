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


###############################################################################################
import functools
import time


def timer(func):
    """ Декоратор-таймер """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} скорость {runtime:.7f} сек.")
        return result
    return _wrapper


####################################################################
""" Задание a) Заполнение списка и словаря """
@timer
def fill_list(n):
    """ Сложность O(n) - Линейная"""
    new_list = []           # O(1) - Константная
    for i in range(n):      # O(n) - Линейная
        new_list.append(i)  # O(1) - Константная
    return new_list         # O(1) - Константная


@timer
def fill_dict(n):
    """ Сложность O(n) - Линейная"""
    new_dict = []                           # O(1) - Константная
    for i in range(n):                      # O(n) - Линейная
        new_dict.append(f'{i}:{i ** 2}')    # O(1) - Константная
    return new_dict                         # O(1) - Константная


print(fill_list(1000))    # my_list скорость 0.0006014 сек.
print(fill_dict(1000))    # my_dict скорость 0.0015010 сек.
print(fill_list(10000))   # my_list скорость 0.0045712 сек.
print(fill_dict(10000))   # my_dict скорость 0.0100847 сек.

"""
Список заполняется быстрее потому что чтобы добавить элемент в конец 
достаточно несколько байт записать в заранее выделенную память.
Запись у словаря будет медленнее, потому что надо посчитать хэш
и аккуратно всё в память по индексам положить.   
"""

###########################################################################
""" Задание b) получение элемента списка и словаря"""
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
my_dict_1 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}
my_dict_2 = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
             11: '1', 12: '2', 13: '3', 14: '4', 15: '5', 16: '6', 17: '7', 18: '8', 19: '9', 20: '10',
             21: '1', 22: '2', 23: '3', 24: '4', 25: '5', 26: '6', 27: '7', 28: '8', 29: '9', 30: '10',
             31: '1', 32: '2', 33: '3', 34: '4', 35: '5', 36: '6', 37: '7', 38: '8', 39: '9', 40: '10',
             41: '1', 42: '2', 43: '3', 44: '4', 45: '5', 46: '6', 47: '7', 48: '8', 49: '9', 50: '10'}


@timer
def get_list(lst):
    """ Сложность O(n) - Линейная """
    for n in range(len(lst)):   # O(n) - Линейная
        return lst              # O(1) - Константная


@timer
def get_dict(d):
    """ Сложность O(n)  - Линейная"""
    for key, value in d.items():    # O(n) - Линейная
        return d                    # O(1) - Константная


print(get_list(my_list_1))  # get_list скорость 0.0000065 сек.
print(get_dict(my_dict_1))  # get_dict скорость 0.0000039 сек.
print(get_list(my_list_2))  # get_list скорость 0.0000013 сек.
print(get_dict(my_dict_2))  # get_dict скорость 0.0000007 сек.

""" Элементы получить быстрее из словаря, т.к. в словаре поиск элементов идет по ключу, 
   а в списке перебираются все элементы"""

##############################################################################
""" с) Удаление элемента списка и словаря """


@timer
def del_list(lst):
    """ Сложность O(n)  - Линейная"""
    for i in range(len(lst)):  # O(n) - Линейная
        lst.pop()              # O(1) - Константная
    return lst                 # O(1) - Константная


@timer
def del_dict(d):
    """ Сложность O(n)  - Линейная"""
    for i in list(d):   # O(n) - Линейная
        del d[i]        # O(1) - Константная
    return d            # O(1) - Константная


print(del_list(my_list_1))  # del_list скорость 0.0000045 сек.
print(del_dict(my_dict_1))  # del_dict скорость 0.0000042 сек.
print(del_list(my_list_2))  # del_list скорость 0.0000060 сек.
print(del_dict(my_dict_2))  # del_dict скорость 0.0000053 сек.

""" Удаление из словаря происходит быстрее, так как перебор элементов в словаре идет по ключу, а при удалении элементов
из списка происходит смещение всего списка и перебор всех его элементов"""
