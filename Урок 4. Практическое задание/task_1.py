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


num_100 = range(1, 100)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
            print(new_arr)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    print(new_arr)
    return new_arr


func_2(num_100)
func_1(num_100)
# count_time_1 = timeit.timeit('func_1(num_100)', setup='from __main__ import func_1, num_100')
# count_time_2 = timeit.timeit('func_2(num_100)', setup='from __main__ import func_2, num_100')
#
# print(count_time_1, "Время 1 функции")
# print(count_time_2, "Время 2 функции")

# Аналитика
# 18.63887419970706 Время 1 функции
# 16.245855399873108 Время 2 функции
# используем генератор списка для ускорения работы, как видно по замерам, время работы улучшили.
