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

# решение с помощью перебора в цикле
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# ls
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums1 = [i for i in range(10)]
nums2 = [i for i in range(100)]
nums3 = [i for i in range(1000)]

print(timeit("func_1(nums1)", globals=globals(), number=1000))  # 0.0012282999999999877
print(timeit("func_2(nums1)", globals=globals(), number=1000))  # 0.0023841
# время выполнения меньше при использовании традиционного итератора

print(timeit("func_1(nums2)", globals=globals(), number=1000))  # 0.007638999999999993
print(timeit("func_2(nums2)", globals=globals(), number=1000))  # 0.006498600000000007

print(timeit("func_1(nums3)", globals=globals(), number=1000))  # 0.0908205
print(timeit("func_2(nums3)", globals=globals(), number=1000))  # 0.07646
# время выполнения меньше при использовании ls (спискового включения)

# Для небольших массивов (около 10 элементов ибыстрее будет выполняться код с перебором в цикле,
# для больших массивов быстрее выполняется код с использованием ls.

