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


def time_check(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


def average_time_check(function):
    def wrapper(*args, **kwargs):
        time_lst = []
        for i in range(10):
            start_time = time.time()
            function(*args, **kwargs)
            end_time = time.time()
            timing = end_time - start_time
            time_lst.append(timing)
        print(f' среднее время при запуске 10 раз {function} = {sum(time_lst) / 10}')
    return wrapper


#  -- Пункт a:
@average_time_check
def fill_lst(num, lst):    # O(1)
    for i in range(num):   # O(1)
        el = i             # O(1)
        lst.append(el)     # O(1)
    return lst             # O(1)


@average_time_check
def fill_dict(num, dict_obj):   # O(1)
    for i in range(num):        # O(1)
        dict_obj[i] = i         # O(1)
    return dict                 # O(1)


fill_lst(10**6, [])
fill_dict(10**6, {})

"""
среднее время при запуске 10 раз <function fill_lst at 0x0000028C28D9A440> = 0.13906598091125488
среднее время при запуске 10 раз <function fill_dict at 0x0000028C28D9A560> = 0.1078822135925293

В данном примере список заполняется при помощи метода append, а словарь заполняется при помощи доступа по индексу, 
поэтому время заполнения словаря больше. Так же в этом примере в функцию передается пустой список или словарь, если 
создавать объекты внутри функций создание словаря занимало бы больше времени чем создание списка.  
"""


# -- Пункт - b
@average_time_check
def take_lst_el(lst_obj, value):    # O(N)
    for el in lst_obj:              # O(N)
        if el == value:             # O(1)
            return el               # O(1)


@average_time_check
def take_dict_el(dict_obj, value):  # O(N)
    for v in dict_obj.values():     # O(N)
        if v == value:              # O(1)
            return v                # O(1)


snd_lst = [el for el in range(10**7)]
snd_dict = {n: n for n in range(10**7)}

take_lst_el(snd_lst, 15)
take_dict_el(snd_dict, 15)

"""
среднее время при запуске 10 раз <function take_lst_el at 0x000001C6BFF3A7A0> = 0.001562509536743164
среднее время при запуске 10 раз <function take_dict_el at 0x000001C6BFF3A8C0> = 0.0031246662139892576
При возвращении значения из словаря тратиться больше времени, чем при возвращении значения из списка,
т.к. словарь хранит в себе помимо значений еще и ключи. В данном примере не используется доступ по индексу
методы pop, что могло бы ускорить получение значения.
"""


# -- Пункт c:
@average_time_check
def remove_from_lst(lst_obj, val):  # O(N)
    for el in lst_obj:              # O(N)
        if el == val:               # O(1)
            lst_obj.remove(el)      # O(N)
    return lst_obj                  # O(1)


@average_time_check
def remove_from_dict(dict_obj, val):    # O(N)
    new_dict_obj = dict_obj.copy()      # O(1)
    for k, v in dict_obj.items():       # O(N)
        if v == val:                    # O(1)
            del new_dict_obj[k]         # O(1)
    return new_dict_obj                 # O(1)


remove_from_lst(snd_lst, 256)
remove_from_dict(snd_dict, 256)
"""
среднее время при запуске 10 раз <function remove_from_lst at 0x000001C56D58A9E0> = 0.482387900352478
среднее время при запуске 10 раз <function remove_from_dict at 0x000001C56D58AB00> = 1.1064233303070068

При одинаковой сложности с точки зрения O-нотации, удаление элемента из словаря занимает больше времени,
т.к. в цикле for для словаря приходится перебирать не только значения values, но и keys.
"""
