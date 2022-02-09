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

nums_list = [el for el in range(500000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""
Аналитика: В func_2 мы убрали привязанность к индексу, длине листа, и шли итеративно по списку 
проверяя по элементное деление на 2 без остатка
Эффект: скорость выполнения увеличилось в полтора раза плюс меньше код
"""


def func_2(nums):
    new_arr = []
    for el in nums:
        if el % 2 == 0:
            new_arr.append(el)
    return new_arr


"""
Аналитика: Тут мы использовали логику func_2 но в виде list comprehension (lc)
Эффект: скорость выполнения увеличилось в полтора раза по сравнению с func_2 и в 2 раза по сравнению с func_1,
плюс избавились от функции и все операции выполнили одной строкой
"""

lc = [el for el in nums_list if el % 2 == 0]

print(
    timeit(
        "func_1(nums_list)",
        globals=globals(),
        number=1000
    )
)

print(
    timeit(
        "func_2(nums_list)",
        globals=globals(),
        number=1000
    )
)

# Замер lc
print(
    timeit(
        '[el for el in nums_list if el % 2 == 0]',
        globals=globals(),
        number=1000
    )
)
