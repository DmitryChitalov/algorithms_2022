import time
from random import sample, randrange


# Декоратор для расчёта времени работы функции
def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Время работы функции "{function.__name__}" - {time.perf_counter() - start_time}')
        return res

    return wrapped


# A-1. Функция для заполнения списка n элементами
@time_of_function
def filling_lst(n):  # O(n)
    lst = sample(range(1, 100000), n)  # O(n)
    return lst  # O(1)


# A-2. Функция для заполнения словаря n элементами
@time_of_function
def filling_dict(n):  # O(n)
    dct = {}  # O(1)
    for k in range(n):  # O(n)
        k = randrange(1, 1000000)  # O(1)
        v = 2 * k  # O(1)
        dct[k] = v  # O(1)
    return dct  # O(1)

