"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import Timer


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
    t1 = Timer(stmt='func_1(num)', setup='from __main__ import func_1, num')
    print('Время func_1', t1.timeit(number=100))

    t2 = Timer(stmt='func_2(num)', setup='from __main__ import func_2, num')
    print('Время func_2', t2.timeit(number=100))

    """
        Время func_1 0.003659700000000002
        Время func_2 0.002307500000000004 - В функции вместо цикла for применен List Comprehension: создание списка и 
        его заполнение происходит одновременно. 
    """
