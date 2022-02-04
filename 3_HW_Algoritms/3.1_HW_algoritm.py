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
from time import time

# создадим переменную  для кол-ва добавляемых элементов
check_num = 1000000


# декоратор подсчета времени
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        print(f"{func} {end - start}")
        return return_value

    return wrapper


""" a) Результаты заполнения списка и словаря показыват, что использование comprehension ускоряет заполнение. 
Но список заполняется быстрее как классическим способом так и 'продвинутым' примерно в 2.5 раза. Хотя у всех функций 
заполнение будет O(n) Возможно !? Это связано со структурой хранения данных, в список элементы добавляются 
последовательно без проверки, а в словарь элементы добавляются с проверкой так как не может быть два одинаковых ключа"""


# Классический вариант заполнения списка
# O(1)
@time_decorator
def completion_list():
    my_list = []  # O(1)
    for i in range(check_num):  # O(1)
        my_list.append(i)  # O(1)
    return my_list


completion_list()


# List comprehensions
# O(1)
@time_decorator
def completion_lc():
    return [i for i in range(check_num)]  # O(1)


# список для взаимодействия
list1 = completion_lc()


# классический вариант заполнения словаря
# O(1)
@time_decorator
def completion_dict():
    my_dict = {}  # O(1)
    for num1 in range(check_num):  # O(1)
        my_dict[num1] = num1  # O(1)
    return my_dict


completion_dict()


# Dict comprehension
# O(1)
@time_decorator
def completion_dc():
    return {i: i for i in range(check_num)}  # O(n)


dict1 = completion_dc()

"""б) По результатам замеров списки во всех отношениях быстрее """

print('------пункт Б------')


# Изменение элементов списка
# O(n)
@time_decorator
def change_list(my_list):
    for i, val in enumerate(my_list):
        my_list[i] = val + val
    return my_list


change_list(list1)


# удаление элемента из списка
# O(1)
@time_decorator
def del_el_list(my_list):
    for i in range(10000):
        my_list.pop()
    return my_list


del_el_list(list1)


# Изменение словаря
# O(n)
@time_decorator
def change_dict(my_dict):
    for key, value in enumerate(my_dict):
        my_dict[key] = value + value
    return my_dict


change_dict(dict1)


# удаление элементов в словаре
# O(1)
@time_decorator
def del_el_dict(my_dict):
    for i in range(10000):
        my_dict.popitem()
    return my_dict


del_el_dict(dict1)
