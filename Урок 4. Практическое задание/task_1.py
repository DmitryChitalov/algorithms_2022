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
from random import sample

def func_1(nums: list) -> list:
    # Вернуть массие индексов четных элементов полученного массива
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums: list) -> list:
    # Вернуть массие индексов четных элементов полученного массива
    return [index for index in range(len(nums)) if not nums[index] % 2]

if __name__ == "__main__":
    nums = sample(range(10000), 1000)
    print(f"func_1 выполнился за время: {timeit('func_1(nums)', number=10000, globals=globals())}")
    print(f"func_2 выполнился за время: {timeit('func_2(nums)', number=10000, globals=globals())}")

    # func_1 выполнился за время: 3.0955781230004504
    # func_2 выполнился за время: 1.7884314139955677
    # func_2 отрабатывает быстрее, так как не вызывает append() на каждой итерации.