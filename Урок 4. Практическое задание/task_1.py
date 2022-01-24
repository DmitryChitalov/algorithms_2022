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
# 1) reqular_circle - самый медленный вариант
# 2) List Comprehension дает небольшое усрорение.
# 3) Можно ускорить работу функции через numpy в 4 раза, но требуется входные данные 
# сначала сконвертировать, плюс потеря времени на компиляцию функции. 
# Зато функция потом быстро выполняется.
# Результаты замеров:
# foo_reqular_circle---min time:     0.8832532999804243
# foo_list_comprehension---min time: 0.7768935000058264
# foo_compile_with_numpy---min time: 0.2066441000206396
# ==============================================================================

import numbers
from timeit import timeit, default_timer, repeat
import numpy as np
import numba
from numba import jit
from numba import types
import math


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
    new_arr = [i for i, num in enumerate(nums, 0) if num % 2 == 0]
    return new_arr


funcs.append("foo_list_comprehension")

# ====================================
@jit(nopython=True)
def foo_compile_with_numpy(nums):
    new_arr = [i for i, num in enumerate(nums, 0) if num % 2 == 0]
    return new_arr

# ====================================
# ====================================
for func in funcs:
    print(f'{f"{func}---min time: ":35}'+
          str(min(repeat(f'{func}(l)', default_timer, globals=globals(), repeat=3, number=1))))

# ====================================          
l1=np.asarray(l, dtype=np.int8)
print(f'{"foo_compile_with_numpy---min time: ":35}'+
          str(min(repeat(f'foo_compile_with_numpy(l1)', default_timer, globals=globals(), repeat=3, number=1))))




