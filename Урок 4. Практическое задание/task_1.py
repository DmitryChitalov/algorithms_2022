"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import default_timer


def time_it(func):
    def wrapper(numb):
        start_time = default_timer()
        func(numb)
        # правая отсечка времени и результат
        print(default_timer() - start_time)
        # логгирование
        # и любые другие действия
    return wrapper


@time_it
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@time_it
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


massive = (1, 2, 3, 4, 5, 6, 7)
func_1(massive)     # 3.300000000004688e-06
func_2(massive)     # 2.799999999997249e-06


# оптимизация цикла с помощью list comprehensions дает ощутимое ускорение выполнения функции

