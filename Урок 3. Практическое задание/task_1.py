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
import random

# Функция декоратор для измерения времени выполнения функции-аргумента.
def check_time(func):
    def wrap(*args):
        time_start = time.time()
        ret = func(*args)
        time_end = time.time()
        print(func.__name__, time_end - time_start)
        return ret

    return wrap

list_data = [num for num in range(10000000)]
#print(list_data)

list_ex = []
dict_ex = {}

# Пункт a
# Заполнение списка через append.
# Сложность O(n).
@check_time
def fill_list(list_ex, list_data):
    for i in list_data:               # O(n))
        list_ex.append(i)             # O(1)

    return list_ex

# Заполнение списка через insert.
# Сложность O(n).
@check_time
def fill_list_1(list_ex, list_data):
    for i in list_data:               # O(n))
        list_ex.insert(0, i)          # O(1)

    return list_ex

# Заполнение словаря через setdefault.
# Сложность O(n).
@check_time
def fill_dict(dict_ex, list_data):
    for i in range(10000000):                        # O(n)
        dict_ex.setdefault(i, list_data[i])      # O(1)

    return dict_ex

fill_list(list_ex, list_data)
# print(list_ex)
# list_ex = []
# fill_list_1(list_ex, list_data)
# print(list_ex)
fill_dict(dict_ex, list_data)
# print(dict_ex)

'''
Заполнение списка из 100000 элементов через append составило - 0.01595759391784668.
Заполнение списка из 100000 элементов через insert составило - 5.525012493133545.
Заполнение солваря из 100000 элементов через setdefault составило - 0.026928186416625977.
Наиболее быстрый способ заполнения списка через append.
Заполнение списка через insert работает очень медленно, уже на 100000 элементов
И в целом заполнение словаря более длительный процесс в связи с созданием ХЕШ-значения KEYs, примерно в 2 раза больше.
'''

# Пункт b

# Пункт b 
# Получение элемента списка по индексу.

n = random.randint(0, 10000000)

# Сложность O(n).
@check_time
def get_el_list(list_ex):
    for i in list_ex:       # O(n)
        _ = i               # O(1)

# Полунчение элемента словаря через get.
# Сложность O(n).
@check_time
def get_el_dict(dict_ex):
    for i in range(10000000):  # O(n)
        _ = dict_ex[i]         # O(1)

get_el_list(list_ex)
#print(get_el_list(list_ex))
get_el_dict(dict_ex)
#print(get_el_dict(dict_ex))

# Время извлечения списка из 10000000 элементов через append составило - 0.25221967697143555.
# Время извлечения словаря из 10000000 элементов через append составило - 0.8499264717102051.
# Время извлечения элементов словаря больше чем списка примерно в 3 раза, видимо сказывается цикл и метод получения!

# Пункт c
# Удаление элемента списка по индексу.

n = random.randint(0, 10000000)

# Сложность O(n).
@check_time
def del_el_list(list_ex):
     for i in list_ex:       # O(n)
        list_ex.pop()        # O(1)

# Удаление элемента словаря по ключу.
# Сложность O(n).
@check_time
def del_el_dict(dict_ex):
    for i in range(10000000):  # O(n)
        dict_ex.pop(i)         # O(1)
    

del_el_list(list_ex)
#print(del_el_list(list_ex))
del_el_dict(dict_ex)
#print(del_el_dict(dict_ex))

# Время удаления списка из 10000000 элементов через append составило - 0.31475400924682617.
# Время удаления списка из 10000000 элементов через append составило - 1.3295505046844482.
# Время удаления элементов словаря больше чем списка примерно в 3 раза!
