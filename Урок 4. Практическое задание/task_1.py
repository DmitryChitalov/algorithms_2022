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


# Вместо функции append применим списковое включение
def func_2(nums):
    return [el for el in nums if el % 2 == 0]


test_nums = [el for el in range(1000)]

# 1000 итераций
print(timeit("func_1(test_nums[:])", globals=globals(), number=1000))
print(timeit("func_2(test_nums[:])", globals=globals(), number=1000))

# 10000 итераций
print(timeit("func_1(test_nums[:])", globals=globals(), number=10000))
print(timeit("func_2(test_nums[:])", globals=globals(), number=10000))

"""
Результаты
1000:
0.07687350001651794
0.04508549999445677
10000:
0.8112455999944359
0.446218500030227
С применением спискового включения время выполения снизилось примерно на 40% 
"""
