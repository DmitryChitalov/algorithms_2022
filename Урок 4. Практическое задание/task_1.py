"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit, default_timer, repeat


# Исходный код
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = list(range(1000))
print(func_1(nums))

print(timeit(stmt='func_1(nums)', globals=globals(), timer=default_timer, number=1000))  # вариант записи 1
print(timeit('func_1(nums)', 'from __main__ import func_1, nums', default_timer, 1000))  # вариант записи 2
print(repeat('func_1(nums)', 'from __main__ import func_1, nums', default_timer, 3, 1000))


# Замеры
# 0.1040188999613747 сек

# -----------------------------------------------------------------------------------------------------------------
# Оптимизированный код
def func_2(nums):
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


nums = list(range(1000))
print(func_2(nums))

print(timeit('func_2(nums)', 'from __main__ import func_2, nums', default_timer, 1000))
print(repeat('func_2(nums)', 'from __main__ import func_2, nums', default_timer, 3, 1000))

# Замеры
# 0.04363650002051145 сек

# ---------------------------------------------------------------------------------------------------------------
# Выводы
# Выражение list comprehension - быстрее чем итератор с функцией append
