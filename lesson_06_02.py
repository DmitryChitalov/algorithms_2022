from memory_profiler import profile
# Курс основ, 1 урок
# В func_2 заменила список на генератор, считаю сумму чисел без создания списка. Это позволило сократить объем памяти
# с 47.4375 MiB до 21.3203 MiB.


@profile(precision=4)
def func_1():
    numbers = []
    for i in range(1, 10 ** 6, 2):
        if i % 2 != 0:
            number = i ** 3
            numbers.append(number)
    # Создаю список чисел, делящихся на 7 без остатка и вычисляю их сумму
    new_numbers = []
    for item in numbers:
        num = item
        sum_num = 0
        while num % 10 != 0:
            sum_num += num % 10
            num = num // 10
        if sum_num % 7 == 0:
            new_numbers.append(item)
    print(sum(new_numbers))


func_1()
"""
Result = 19565126966864989390401
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4  19.2383 MiB  19.2383 MiB           1   @profile(precision=4)
     5                                         def func_1():
     6  19.2461 MiB   0.0078 MiB           1       numbers = []
     7  46.2656 MiB -698.2891 MiB      500001       for i in range(1, 10 ** 6, 2):
     8  46.2656 MiB -698.3164 MiB      500000           if i % 2 != 0:
     9  46.2656 MiB -676.1289 MiB      500000               number = i ** 3
    10  46.2656 MiB -693.2734 MiB      500000               numbers.append(number)
    11                                             # Создаю список чисел, делящихся на 7 без остатка и вычисляю их сумму
    12  46.2656 MiB   0.0000 MiB           1       new_numbers = []
    13  47.4336 MiB -76419.4375 MiB      500001       for item in numbers:
    14  47.4336 MiB -76419.4375 MiB      500000           num = item
    15  47.4336 MiB -76419.4375 MiB      500000           sum_num = 0
    16  47.4336 MiB -728922.2930 MiB     4825909           while num % 10 != 0:
    17  47.4336 MiB -652502.7852 MiB     4325909               sum_num += num % 10
    18  47.4336 MiB -652502.8008 MiB     4325909               num = num // 10
    19  47.4336 MiB -76419.5156 MiB      500000           if sum_num % 7 == 0:
    20  47.4336 MiB -10917.0391 MiB       74483               new_numbers.append(item)
    21  47.4375 MiB   0.0039 MiB           1       print(sum(new_numbers))
"""


@profile(precision=4)
def func_2():
    numbers = ((i ** 3) for i in range(1, 10 ** 6, 2))
    # Создаю список чисел, делящихся на 7 без остатка и вычисляю их сумму
    new_numbers = 0
    for item in numbers:
        num = item
        sum_num = 0
        while num % 10 != 0:
            sum_num += num % 10
            num = num // 10
        if sum_num % 7 == 0:
            new_numbers += item
    print(new_numbers)


func_2()
"""
Result - 19565126966864989390401
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    27  21.3203 MiB  21.3203 MiB           1   @profile(precision=4)
    28                                         def func_2():
    29  21.3203 MiB   0.0000 MiB     1000003       numbers = ((i ** 3) for i in range(1, 10 ** 6, 2))
    30                                             # Создаю список чисел, делящихся на 7 без остатка и вычисляю их сумму
    31  21.3203 MiB   0.0000 MiB           1       new_numbers = 0
    32  21.3203 MiB   0.0000 MiB      500001       for item in numbers:
    33  21.3203 MiB   0.0000 MiB      500000           num = item
    34  21.3203 MiB   0.0000 MiB      500000           sum_num = 0
    35  21.3203 MiB   0.0000 MiB     4825909           while num % 10 != 0:
    36  21.3203 MiB   0.0000 MiB     4325909               sum_num += num % 10
    37  21.3203 MiB   0.0000 MiB     4325909               num = num // 10
    38  21.3203 MiB   0.0000 MiB      500000           if sum_num % 7 == 0:
    39  21.3203 MiB   0.0000 MiB       74483               new_numbers += item
    40  21.3203 MiB   0.0000 MiB           1       print(new_numbers)
    41  21.3203 MiB   0.0000 MiB           1       del numbers
"""