"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import default_timer, timeit


def time_it(func):
    def wrapper(numb):
        start_time = default_timer()
        func(numb)
        print(default_timer() - start_time)

    return wrapper


@time_it
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return print(new_arr)


@time_it
def func_2(nums):
    new_arr = []
    [new_arr.append(i) if nums[i] % 2 == 0 else '' for i in range(len(nums))]
    return print(new_arr)


func_1([1, 2, 3, 4, 5, 6])
func_2([1, 2, 3, 4, 5, 6])
# LC оказался медленее простого условия в цикле