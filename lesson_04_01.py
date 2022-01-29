from timeit import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Сделайте замеры времени выполнения кода с помощью модуля timeit


print(f'Замер времени функции func_1: {timeit("func_1", "from __main__ import func_1", number=1000)}')

# Попробуйте оптимизировать код, чтобы снизить время выполнения
numbers = [randint(1, 100) for i in range(randint(1, 100))]


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Проведите повторные замеры
print(f'Замер времени функции func_2: {timeit("func_2", "from __main__ import func_2", number=1000)}')


def func_3(nums):
    result = []
    for idx, item in enumerate(nums):
        if item % 2 == 0:
            result.append(idx)
    return result


print(f'Замер времени функции func_3: {timeit("func_3", "from __main__ import func_3", number=1000)}')

"""
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
Замер времени функции func_1: 1.359999999999903e-05
Замер времени функции func_2: 1.1899999999998717e-05
Замер времени функции func_3: 1.1799999999999311e-05
В func_2 я использовала lc, что сократило время работы с 1.359999999999903e-05, до 1.1899999999998717e-05
В func_3 я использовала встроенную функцию enumerate, что сократило время работы с 1.1099999999999999e-05, 
до 1.1000000000000593e-05
"""