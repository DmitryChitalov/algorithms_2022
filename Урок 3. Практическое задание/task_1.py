"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

"""
import random
import string
import time


def time_spent(func):
    import time
    def wrapper(*args):
        start_time = time.time()  # O(1)
        some_func = func(*args)  # O(1)
        end_time = time.time()  # O(1)
        print(f"Time for {func} = {end_time - start_time}")  # O(1)
        return some_func

    return wrapper


# список будем заполнять либо строковой, либо числовой переменной
# в зависимости от случайно сгенерированного числа (0 - для строки, 1 - для числа)

def generate_random_string(length):
    letters = string.ascii_lowercase  # O(1)
    rand_string = ''.join(random.choice(letters) for i in range(length))  # O(n)
    return rand_string


# Сложность O(n^2)
@time_spent
def list_fill_in(list_length):
    res = []  # O(1)
    for i in range(list_length):  # O(n)
        def_code = random.randint(0, 1)  # O(1)
        if def_code == 0:  # O(1)
            str_length = random.randint(1, 20)  # O(1)
            res.append(generate_random_string(str_length))  # O(1)
        else:
            res.append(random.randint(-100000, 500000))  # O(1)
    return res

#
list_fill_in(5000)


# Сложность O(n^2)
@time_spent
def dict_fill_in(dict_length):
    res = {}  # O(1)
    for i in range(0, dict_length):  # O(n)
        def_code = random.randint(0, 1)  # O(1)
        if def_code == 0:  # O(1)
            str_length = random.randint(1, 20)  # O(1)
            res[i + 1] = generate_random_string(str_length)  # O(1)
        else:
            res[i + 1] = random.randint(-100000, 500000)  # O(1)
    return res


dict_fill_in(5000)
# О нотация одинаковая в обоих случаях,
# но думаю, что заполнение словаря происходит медленнее,
# т.к. дополнительно идет операция хэширования




"""

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
"""


@time_spent
def get_el_from_lst(lst, idx):
    return lst[idx]               # O(1)


@time_spent
def get_el_from_dict(dict, key):
    return dict[key]             # O(1)


list_b = list_fill_in(4000)
dict_b = dict_fill_in(4000)

get_el_from_lst(list_b, 2000)
get_el_from_dict(dict_b, 2000)

# О Нотация в обеих функциях одинаковая, по времени тоже не вижу различий,
# но предполагаю, что функция получения элемента из словаря работает быстрее,
# т.к. словарь это хэшируемый объект




"""

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

# удаление элемента из списка
@time_spent
def del_el_lst(lst, idx):
    lst.pop(idx)             # O(n)
    return lst


# удаление элемента из словаря
@time_spent
def del_el_dict(dict, key):
    del dict[key]            # O(1)
    return dict

del_el_lst(list_b, 350)
del_el_dict(dict_b, 350)

#Вывод: удаление элемента из словаря происходит быстрее,
# но по времени отличия нет
