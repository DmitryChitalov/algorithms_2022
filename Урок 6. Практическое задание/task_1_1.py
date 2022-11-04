"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.
"""
"""Мой код после первого урока по основам, точнее чуть исправленная, пришлось все в функцию затащить, чтоб замерить"""

from memory_profiler import profile


@profile()
def solve():

    def sum_digit(value):
        result = 0

        while value > 0:
            result += value % 10
            value //= 10
        return result

    i = 1
    list_of_cubes = []
    idx = 0
    res1 = 0
    while i < 100000:
        list_of_cubes.append(i ** 3)
        i += 2

    # в этом месте я тогда не понял задание и сложил суммы знаков, а не числа, сумма знаков которых делиться на семь, но в приципе на память это не сильно влияет

    while idx < len(list_of_cubes):
        list_of_cubes[idx] = sum_digit(list_of_cubes[idx])
        idx += 1

    for element in list_of_cubes:
        if element % 7 == 0:
            res1 = res1 + element
    print(res1)


solve()

"""Это оптимизированный код"""

@profile()
def solve_upd():
    summa = 0
    list_of_cubes = [i ** 3 for i in range(1, 100001) if i % 2 != 0]
    tuple_of_cubes = tuple(list_of_cubes)
    del list_of_cubes

    def sum_digit(value):
        result = 0
        while value > 0:
            result += value % 10
            value //= 10
        return result

    for i in tuple_of_cubes:
        if sum_digit(i) % 7 == 0:
            summa += i
    return summa


print(solve_upd())

""" Пришлось увеличить количество цифр в списках, чтобы была видна разница
Filename: C:\python_projects\Algoritm\lesson_6\task_1\task_1_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     19.8 MiB     19.8 MiB           1   @profile()
    13                                         def solve():
    14                                         
    15     22.8 MiB -16162.5 MiB       50001       def sum_digit(value):
    16     22.8 MiB -16162.5 MiB       50000           result = 0
    17                                         
    18     22.8 MiB -258599.7 MiB      756690           while value > 0:
    19     22.8 MiB -242437.2 MiB      706690               result += value % 10
    20     22.8 MiB -242437.2 MiB      706690               value //= 10
    21     22.8 MiB -16162.5 MiB       50000           return result
    22                                         
    23     19.8 MiB      0.0 MiB           1       i = 1
    24     19.8 MiB      0.0 MiB           1       list_of_cubes = []
    25     19.8 MiB      0.0 MiB           1       idx = 0
    26     19.8 MiB      0.0 MiB           1       res1 = 0
    27     22.8 MiB      0.0 MiB       50001       while i < 100000:
    28     22.8 MiB      2.5 MiB       50000           list_of_cubes.append(i ** 3)
    29     22.8 MiB      0.4 MiB       50000           i += 2
    30                                         
    31                                             # в этом месте я тогда не понял задание и сложил суммы знаков, а не числа, сумма знаков которых делиться на семь, но в приципе на память это не сильно влияет
    32                                         
    33     22.8 MiB -16163.7 MiB       50001       while idx < len(list_of_cubes):
    34     22.8 MiB -16163.7 MiB       50000           list_of_cubes[idx] = sum_digit(list_of_cubes[idx])
    35     22.8 MiB -16163.7 MiB       50000           idx += 1
    36                                         
    37     21.6 MiB     -1.2 MiB       50001       for element in list_of_cubes:
    38     21.6 MiB      0.0 MiB       50000           if element % 7 == 0:
    39     21.6 MiB      0.0 MiB        5858               res1 = res1 + element
    40     21.6 MiB      0.0 MiB           1       print(res1)


Filename: C:\python_projects\Algoritm\lesson_6\task_1\task_1_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     20.7 MiB     20.7 MiB           1   @profile()
    48                                         def solve_upd():
    49     20.7 MiB      0.0 MiB           1       summa = 0
    50     22.7 MiB      2.0 MiB      100003       list_of_cubes = [i ** 3 for i in range(1, 100001) if i % 2 != 0]
    51     22.7 MiB      0.0 MiB           1       tuple_of_cubes = tuple(list_of_cubes)
    52     22.7 MiB      0.0 MiB           1       del list_of_cubes
    53                                         
    54     22.8 MiB  -1394.2 MiB       50001       def sum_digit(value):
    55     22.8 MiB  -1394.2 MiB       50000           result = 0
    56     22.8 MiB -22307.5 MiB      756690           while value > 0:
    57     22.8 MiB -20913.3 MiB      706690               result += value % 10
    58     22.8 MiB -20913.3 MiB      706690               value //= 10
    59     22.8 MiB  -1394.2 MiB       50000           return result
    60                                         
    61     22.8 MiB  -1394.2 MiB       50001       for i in tuple_of_cubes:
    62     22.8 MiB  -1394.2 MiB       50000           if sum_digit(i) % 7 == 0:
    63     22.8 MiB   -159.9 MiB        5858               summa += i
    64     22.7 MiB     -0.1 MiB           1       return summa


1409831608061185538

Process finished with exit code 0
"""
