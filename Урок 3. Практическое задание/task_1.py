"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: получения и удаления элемента.
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


# Пункт a
def time_of_func(func):
    def f(*args, **kwargs):
        start_time = time.perf_counter_ns()
        res = func(*args, **kwargs)
        print(f'{func}:{time.perf_counter_ns() - start_time}')
        return res

    return f


@time_of_func
def dict_update():
    for i in range(10000):  # O(n)
        test_dict[i] = f'value:{i}'  # O(1)
    return test_dict


@time_of_func
def list_append():
    for i in range(10000):  # O(n)
        test_list.append(i)  # O(1)
    return test_list


test_dict = {}
test_list = []
dict_update()
list_append()

# Сложности функций одинаковые.
# Заполняется дольше словарь, т.к. требуется больше времени для хэширования ключей в словаре.


# Пункт b

# Пункт b
@time_of_func
def dict_get(d):
    for key in d:  # O(n)
        print(d[key])  # O(1)
    return d


@time_of_func
def list_get(s):
    for i in s:  # O(n)
        print(i)  # O(1)
    return s


@time_of_func
def dict_pop(d):
    for i in range(10000):    # O(n)
        d.popitem()           # O(1)
    return d


@time_of_func
def list_pop(s):
    for i in range(len(s)):   # O(n)
        s.pop(0)              # O(n), зависит от индекса(для s.pop(-1) - O(1))
    return s

# dict_pop(test_dict)
# list_pop(test_list)
# dict_get(test_dict)
# list_get(test_list)


# Cложности функций одинаковые.
# Но поиск элементов через хэш быстрее, чем поиск по индексу.
# Затраты на удаление больше элементов словаря больше, тк удаление по индексу дольше, чем через хэш