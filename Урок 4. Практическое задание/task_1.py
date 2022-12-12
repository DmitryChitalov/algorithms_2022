"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
import timeit
import time


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0 and nums[i] != 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr, counter = [], -1
    for i in nums:
        counter += 1
        if i % 2 == 0 and nums[i] != 0:
            new_arr.append(counter)
    return new_arr


def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0 and nums[i] != 0]
    return new_arr


massif = [i for i in range(1000)]

res_func_1, res_func_2, res_func_3, n = [], [], [], 0
while n < 20:
    res_func_1.append(timeit.timeit(stmt='func_1(massif)', setup='from __main__ import func_1, massif', number=1000))
    time.sleep(1)
    res_func_2.append(timeit.timeit(stmt='func_2(massif)', setup='from __main__ import func_2, massif', number=1000))
    time.sleep(1)
    res_func_3.append(timeit.timeit(stmt='func_3(massif)', setup='from __main__ import func_3, massif', number=1000))
    time.sleep(1)
    n += 1
print(sum(res_func_1) / len(res_func_1), sum(res_func_2) / len(res_func_2), sum(res_func_3) / len(res_func_3), sep='\n')

'''
res_func_1 - 0.2018358749919571
res_func_2 - 0.2170171500183642
res_func_3 - 0.18363176498096437
Функция func_2 менее иффективна чем func_1, но func_3 зачастую позказывает результат чуть лучше чем другие функции.
Следует отметить что на скорости выполнения отрицательно сказывается загруженность ресурсов компьютера выполнением
предыдущей функции. Для избежания этого использую задержки.'''
