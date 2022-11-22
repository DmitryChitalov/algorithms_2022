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


# Ф-я декоратор для подсчета среднего времени выполнения функции
def lead_time(func):
    '''
    Ф-я декоратор для подсчета среднего времени выполнения функции
    Количество запусков ф-ии 10000 раз
    :param func:
    :return:
    '''
    import time

    def wrapper(a, b=None):
        n = 1000
        start = time.time()
        for i in range(n):
            result = func(a, b)
        end = time.time()
        average_time = (end - start) / n
        print(f'Среднее время выполнения: {average_time} секунд (при запуске функции {n} раз).')
        return (result, average_time)

    return wrapper


# Задание 1_а
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~ Задание 1_а ~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


@lead_time
def list_completion(a: int, b: int):
    '''
    функция для заполения списка символами таблицы ASCII, начиная с символа
    под номером a и заканчивая b включительно.
    Сложность: O(n)

    :param a:int
    :param b:int
    :return: list
    '''
    list_data = []
    for i in range(a, b):
        list_data.append((i, chr(i)))
    return list_data


# print(list_completion(32, 127))

@lead_time
def dict_completion(a, b):
    '''
        функция для заполения словаря символами таблицы ASCII, начиная с символа
        под номером a и заканчивая b включительно. Номер символа-ключ, символ - значение словаря.
        Сложность: O(n)

        :param a:int
        :param b:int
        :return: dict
        '''
    dict_data = {}
    for i in range(a, b):
        dict_data[i] = chr(i)
    return dict_data


list_data = list_completion(1, 127)
print(list_data)
dict_data = dict_completion(1, 127)
print(dict_data[0])
print(f'Разница в скорости выполнения функций'
      f'({list_data[1]} - {dict_data[1]}) / {list_data[1]} * 100 = {(list_data[1] - dict_data[1]) / list_data[1] * 100} %')
#  Заполнение списка медленнее заполнения словаря

# Задание 1_с
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~ Задание 1_b ~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def lead_time_2(func):
    '''
    Ф-я декоратор для подсчета среднего времени выполнения функции
    Количество запусков ф-ии 10000 раз
    :param func:
    :return:
    '''
    import time

    def wrapper(a):
        n = 1000
        start = time.time()
        for i in range(n):
            result = func(a)
        end = time.time()
        average_time = (end - start) / n
        print(f'Среднее время выполнения: {average_time} секунд (при запуске функции {n} раз).')
        return (result, average_time)

    return wrapper


@lead_time_2
def list_get_elem(a: list):
    '''
    функция для получения значения из списка кортежей

    Сложность: O(n)

    :param a:int
    :param b:int
    :return: list
    '''
    import copy

    copy_a = copy.deepcopy(a)
    result = ''
    for i in range(len(copy_a)):
        el = copy_a[i]
        result += el[1]
    return result


@lead_time_2
def dict_get_elem(a: dict):
    '''
    функция для получения значения из словаря по ключу

    Сложность: O(n)

    :param a:int
    :param b:int
    :return: list
    '''
    import copy

    copy_a = copy.deepcopy(a)
    result = ''
    for i in range(1, len(copy_a) + 1):
        el = copy_a[i]
        result += el
    return result


x = list_get_elem(list_data[0])
print(x)
y = dict_get_elem(dict_data[0])
print(y)
print(f'Разница в скорости выполнения функций'
      f'({x[1]} - {y[1]}) / {x[1]} * 100 = {(x[1] - y[1]) / x[1] * 100} %')
#  Получение элемента из списка медленнее чем из словаря

# Задание 1_с
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~ Задание 1_с ~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


@lead_time_2
def list_pop(a: list):
    '''
    функция для удаления элементов списка
    Сложность: O(n)

    :param a:int
    :param b:int
    :return: list
    '''
    import copy

    copy_a = copy.deepcopy(a)
    result = ''
    while len(copy_a) != 0:
        el = copy_a.pop()
    return


@lead_time_2
def dict_pop(a: dict):
    '''
    функция для удаления элементов словаря
    Сложность: O(n)

    :param a:int
    :param b:int
    :return: list
    '''
    import copy

    copy_a = copy.deepcopy(a)
    while len(copy_a) != 0:
        el = copy_a.popitem()
    return


x = list_pop(list_data[0])
print(x)
y = dict_pop(dict_data[0])
print(y)

print(f'Разница в скорости выполнения функций'
      f'({x[1]} - {y[1]}) / {x[1]} * 100 = {(x[1] - y[1]) / x[1] * 100} %')

#  Удаление элемента из списка медленнее чем из словаря
