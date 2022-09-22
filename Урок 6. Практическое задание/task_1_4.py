#Это файл для четвертого скрипта

from memory_profiler import profile


# Урок 4. Задание 1

@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_1_opt(nums):
    new_list = filter(lambda x: x % 2 == 0, nums)
    return new_list


num = tuple(range(100000))
func_1(num)
func_1_opt(num)

"""
    38     23.4 MiB     23.4 MiB           1   @profile
    39                                         def func_1(nums):
    40     23.4 MiB      0.0 MiB           1       new_arr = []
    41     26.0 MiB      0.0 MiB      100001       for i in range(len(nums)):
    42     26.0 MiB      1.6 MiB      100000           if nums[i] % 2 == 0:
    43     26.0 MiB      1.1 MiB       50000               new_arr.append(i)
    44     26.0 MiB      0.0 MiB           1       return new_arr

Filename: C:\PythonProjects\pythonProject2\ algorithms_2022\Урок 6. Практическое задание\ task_1_4.py
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     24.9 MiB     24.9 MiB           1   @profile
    48                                         def func_1_opt(nums):
    49     24.9 MiB      0.0 MiB           1       new_list = filter(lambda x: x % 2 == 0, nums)
    50     24.9 MiB      0.0 MiB           1       return new_list

    Filter значительно помогает уменьшить использование памяти 

"""