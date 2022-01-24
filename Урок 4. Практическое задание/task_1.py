"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
# ==============================================================================
# === Ответ ====================================================================
# ==============================================================================
# 1) List Comprehension дает ускорение в 2 раза.
# 2) Функция filter ускорение не дает.
# 3) Можно ускорить работу через numpy в 10 раз, но требуется входные данные 
# сначала сконвертировать, плюс потеря времени на компиляцию функции. 
# Зато функция потом быстро выполняется.
# Результаты замеров:
# foo_reqular_circle---min time:     0.9182304000714794
# foo_list_comprehension---min time: 0.49410859995987266
# foo_filter---min time:             0.8611214000266045
# foo_compile_with_numpy---min time: 0.102828299975954
# ==============================================================================

import numbers
from timeit import timeit, default_timer, repeat
import numpy as np
import numba
from numba import jit
from numba import types



l=[i for i in range(10**7)]
funcs = []

# ====================================
def foo_reqular_circle(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


funcs.append("foo_reqular_circle")

# ====================================
def foo_list_comprehension(nums):
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


funcs.append("foo_list_comprehension")

# ====================================
def foo_filter(nums):
    new_arr = list(filter(lambda num: num % 2 == 0, nums))
    return new_arr

funcs.append("foo_filter")

# ====================================
@jit(nopython=True)
def foo_compile_with_numpy(nums):
    new_arr = [num for num in nums if num % 2 == 0]
    return new_arr


# ====================================
for func in funcs:
    print(f'{f"{func}---min time: ":35}'+
          str(min(repeat(f'{func}(l)', default_timer, globals=globals(), repeat=3, number=1))))

# ====================================          
l1=np.asarray(l, dtype=np.int8)
print(f'{"foo_compile_with_numpy---min time: ":35}'+
          str(min(repeat(f'foo_compile_with_numpy(l1)', default_timer, globals=globals(), repeat=3, number=1))))




