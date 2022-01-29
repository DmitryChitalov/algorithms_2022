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

# осуществим обработку элементов списка с условием 
# это нам даст улучшение времени обработки списка 
def func_2(nums):
    new_arr = list(filter(lambda x: x % 2 == 0, nums))
    return new_arr


# получим элемент списка не по его как в (func_1)
# это нам даст улучшение времени обработки списка
def func_3(nums):
    new_arr = []
    for x in nums:
        if int(x) % 2 == 0:
            new_arr.append(nums.index(x))

    return new_arr


# используем list comprehension
# это нам даст улучшение времени обработки списка
def func_4(nums):
    new_arr = [nums.index(x) for x in nums if x % 2 == 0]
    return new_arr


# создадим массив, но при маленьких массивах скорость работы аналогична с func_1
# но при больших массивах скорость будет самая оптимальная
def func_5(nums):
    return [idx for idx, val in enumerate(nums) if val % 2 == 0]


# nums = list(range(200))
nums = [1, 3, 1, 3, 7, 4, 5, 1]

print(func_1(nums))
print(func_2(nums))
print(func_3(nums))
print(func_4(nums))
print(func_5(nums))

print(timeit(stmt='func_1(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_2(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_3(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_4(nums)', globals=globals(), number=1000))
print(timeit(stmt='func_5(nums)', globals=globals(), number=1000))


"""
Результат
[5]
[4]
[5]
[5]
[5]
0.0007029999978840351
0.000811200006864965
0.0009461000154260546
0.0006111999973654747
0.0007057000184431672
""" 
