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


def time_counter(func):
    def wrapper(*args, **kwargs):
        begin = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'На выполнение функции {func.__name__} потребовалось {round((end - begin), 6)} секунд')
        return result

    return wrapper


@time_counter
def fill_list(n):  # O(n)
    return [n for n in range(n)]


@time_counter
def fill_dict(n):  # O(n)
    return {n: n for n in range(n)}


@time_counter
def del_from_list(list_d, start, count):  # O(n)
    [list_d.pop(n) for n in range(start, start + count)]


@time_counter
def del_from_dict(dict_d, start, count):  # O(n)
    [dict_d.pop(n) for n in range(start, start + count)]


@time_counter
def change_list(list_ch: list, start, count, new_value):  # O(n)
    for n in range(start, start + count):
        list_ch[n] = new_value


@time_counter
def change_dict(dict_ch, start, count, new_value):  # O(n)
    for n in range(start, start + count):
        dict_ch[n] = new_value


print("Заполнение!")
test_list = fill_list(100000)
test_dict = fill_dict(100000)
print("Учитывая одинаковую сложность ф-ий заполнения списка и словаря словарю нужно время на создание хэша ключей")
print("Словарю требуется на 80-100% больше времени.")
print("Изменение!")
change_list(test_list, 10, 10000, 1)
change_dict(test_dict, 10, 10000, 1)
print("Операции по изменению эелементов списка и словаря выполняются одинаково быстро.")
print("Удаление!")
del_from_list(test_list, 10000, 1000)
del_from_dict(test_dict, 10000, 1000)
print("Операции по удалению эелементов словаря выполняются на порядок быстрее, потому что при удалении из списка "
      "необходимо много времени на смещение элементов")
