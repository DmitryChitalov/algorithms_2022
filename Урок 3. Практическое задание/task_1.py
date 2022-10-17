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


def counter_time(function):
    def result_time(*args):
        begin = time.perf_counter()
        result = function(*args)
        end = time.perf_counter()
        print(f"Вычисление функции {function.__name__} заняло {end - begin:0.7f} секунд")
        return result

    return result_time()


# Задание № А ----
# Заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность - O(n) линейная

@counter_time
def fill_list(new_list=[]):
    for i in range(10000):  # O(n) линейное
        new_list.append(i)  # O(1) константаное


# Заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность - O(n) линейное


@counter_time
def fill_dict(new_dict={}):
    for i in range(10000):  # O(n) линейное
        new_dict[i] = str(i)  # O(1) константаное


# АНАЛИТИКА -- что заполняется быстрее и почему
# Словарь заполняеться дольше, так как словарь(dict) не использует сдесь своих приемуществ нахождение по ключу
# Вычисление функции fill_list заняло 0.0007704 секунд
# Вычисление функции fill_dict заняло 0.0023727 секунд


# Задание № Б ----
new_list = []
new_dict = {}
for i in range(99999):
    new_list.append(i)
    new_dict[i] = str(i)


# Получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность - O(n) линейная


@counter_time
def get_el_list(new_list=[]):
    for i in new_list:  # O(n) линейное
        if i == new_list[9999]:  # O(1) константаное
            result = new_list[9999]  # O(1) константаное
        return result  # O(1) константаное


# Получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность -  O(n) линейная


@counter_time
def get_el_dict(new_dict={}):
    for i in new_dict:  # O(n) линейное
        if i == 9999:  # O(1) константаное
            result = new_dict[i]  # O(1) константаное
        return result  # O(1) константаное


# АНАЛИТИКА -- что заполняется быстрее и почему
# Быстрее происходить получение элемента списка,
# Так как мы используем цикл, словарь(dict) не использует сдесь своих приемуществ нахождение по ключу,
# И все же словарь быстрее при поиске определенного элемента так как хранит данные в памяти.
# Вычисление функции get_el_list заняло 0.0000028 секунд
# Вычисление функции get_el_dict заняло 0.0000056 секунд


# Задание № С ----
# Удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность - O(n) линейное


@counter_time
def del_el_list(new_list=[]):
    del_el = 9999
    for i in new_list:  # O(n) линейное
        if i == del_el:  # O(1) константаное
            new_list.pop(i)  # O(1) константаное


# Удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
# Сложность - O(n) линейное


@counter_time
def del_el_dict(new_dict={}):
    del_el = 9999
    for i in new_dict:  # O(n) линейное
        if i == del_el:  # O(1) константаное
            new_dict.pop(i)  # O(1) константаное

# АНАЛИТИКА -- что заполняется быстрее и почему
# Быстрее происходить удаление элемента словаря
# Вычисление функции del_el_list заняло 0.0000012 секунд
# Вычисление функции del_el_dict заняло 0.0000009 секунд
