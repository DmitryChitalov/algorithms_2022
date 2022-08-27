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
    return [idx for idx, el in enumerate(nums) if not el % 2]


if __name__ == '__main__':
    num = [i for i in range(100)]
    print('Время func_1', timeit('func_1(num)', globals=globals(), number=100))
    print('Время func_2', timeit('func_2(num)', globals=globals(), number=100))

    """
        Время func_1 0.0032746000000000025
        Время func_2 0.0016747000000000012 - В функции вместо цикла for применен List Comprehension: создание списка и 
        его заполнение происходит одновременно. 
    """
