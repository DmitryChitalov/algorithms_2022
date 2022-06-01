# Задача: сохранить в массиве индексы четных элементов другого массива (Алгоритмы - 4 урок)


from memory_profiler import profile

nums = [i for i in range(100000)]


# @profile
def func_3(nums):
    new_arr = list(i for i in nums if i % 2 == 0)
    return new_arr


func_3(nums)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    31     18.4 MiB     18.4 MiB           1   @profile
    32                                         def func_3(nums):
    33     18.9 MiB      0.6 MiB      150003       new_arr = list(i for i in nums if i % 2 == 0)
    34     18.9 MiB      0.0 MiB           1       return new_arr
"""


# Для оптимизации памяти сгенерировала кортеж вместо списка, а также применила функцию filter


nums = (i for i in range(100000))


@profile
def func_3(nums):
    new_arr = filter(lambda x: x % 2 == 0, nums)
    return new_arr


func_3(nums)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52     16.3 MiB     16.3 MiB           1   @profile
    53                                         def func_3(nums):
    54     16.3 MiB      0.0 MiB           1       new_arr = filter(lambda x: x % 2 == 0, nums)
    55     16.3 MiB      0.0 MiB           1       return new_arr"""
    