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


# традиционный способ - использование цикла
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# использование List Comprehension
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


res = list(range(10000))
print(timeit("func_1(res)", "from __main__ import func_1, res", number=10000)) #  9.78051 сек.
print(timeit("func_2(res)", "from __main__ import func_2, res", number=10000)) # 6.80032 сек.
# Замена цикла for in на List Comprehension позволила ускорить работу кода на 2,9 сек при number=10 000 и range(10000)



