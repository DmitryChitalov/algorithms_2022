"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':

    nums = [n for n in range(1000)]

    time_of_func_1 = timeit("func_1(nums)", globals=globals(), number=10000)
    time_of_func_2 = timeit("func_2(nums)", globals=globals(), number=10000)
    percent = round(time_of_func_2/time_of_func_1*100, 2)
    print("Время выполнения func_1:", time_of_func_1)
    print("Для ускорения алгоритма используем list comprehension")
    print("Время выполнения func_2:", time_of_func_2)
    print(f"Скорость выполнения возрасла на {100-percent}%")


"""
Время выполнения func_1: 0.48619545900000005
Для ускорения алгоритма используем list comprehension
Время выполнения func_2: 0.3827381670000001
Скорость выполнения возрасла на 21.28%

Оптимизированный код эффективнее за счёт использования встроенных методов python.
"""