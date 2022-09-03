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


def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


if __name__ == '__main__':
    my_list = list(range(100))
    print(func_1(my_list))
    print(func_2(my_list))
    print('10 000')
    print('func_1', timeit('func_1(my_list)', globals=globals(), number=10000))
    print('func_2', timeit('func_2(my_list)', globals=globals(), number=10000))
    print('100 000')
    print('func_1', timeit('func_1(my_list)', globals=globals(), number=100000))
    print('func_2', timeit('func_2(my_list)', globals=globals(), number=100000))
    print('1 000 000')
    print('func_1', timeit('func_1(my_list)', globals=globals(), number=100000))
    print('func_2', timeit('func_2(my_list)', globals=globals(), number=100000))

    """
    Результаты замеров:
    10 000
    func_1 0.11818499997025356
    func_2 0.10826660000020638
    100 000
    func_1 1.6905320000369102
    func_2 1.1762571000144817
    1 000 000
    func_1 1.379425999999512
    func_2 0.8937302000122145

    В функции func_2 было использование comprehension, что позволило уменьшить
    время выполнения поставленной задачи и чем больше запусков тем больше 
    заметно ускорение
    """
