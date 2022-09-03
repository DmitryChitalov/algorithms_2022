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

nums_start = [1, 2, 5, 6, 8, 12, 13, 27, 42]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    ind = [nums.index(num) for num in nums if num % 2 == 0]
    return ind


start_time = timeit.default_timer()
print(func_1(nums_start))
print(timeit.default_timer() - start_time)


start_time2 = timeit.default_timer()
print(func_2(nums_start))
print(timeit.default_timer() - start_time2)


"""
Вывод: list comprehension ускорил выполнение перебора перечня значений и как следствие ускорил
выполнение всей функции
"""