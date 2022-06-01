from memory_profiler import profile
# Заменила цикл на функцию map и сократила потребление памяти с 95.7 MiB на 58.1 MiB


@profile
def func_1():
    numbers = [i for i in range(10 ** 6)]
    result = []
    for num in numbers:
        result.append(float(num))
    return result


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.1 MiB     19.1 MiB           1   @profile
     5                                         def func_1():
     6     58.6 MiB  -2346.7 MiB     1000003       numbers = [i for i in range(10 ** 6)]
     7     58.6 MiB      0.0 MiB           1       result = []
     8     95.7 MiB -43502.2 MiB     1000001       for num in numbers:
     9     95.7 MiB -43524.0 MiB     1000000           result.append(float(num))

"""


@profile
def func_2():
    return tuple(map(float, (i for i in range(10 ** 6))))


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     19.1 MiB     19.1 MiB           1   @profile
    26                                         def func_2():
    27     58.1 MiB -28063.0 MiB     2000003       return tuple(map(float, (i for i in range(10 ** 6))))
"""



