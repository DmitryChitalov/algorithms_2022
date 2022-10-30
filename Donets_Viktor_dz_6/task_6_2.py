"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


@profile
def even_odd(numeric, even=0, odd=0):
    if numeric == 0:
        print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    else:
        if (numeric % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(numeric // 10, even, odd)


@profile
def even_odd_1(numeric, even=0, odd=0):
    while numeric != 0:
        if (numeric % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        numeric = numeric // 10
    else:
        print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')


@profile
def wrapper():
    def even_odd_3(numeric, even=0, odd=0):
        if numeric == 0:
            return print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
        else:
            if (numeric % 10) % 2 == 0:
                even += 1
            else:
                odd += 1
            return even_odd_3(numeric // 10, even, odd)
    return even_odd_3


z = int(input('Введите число: '))
even_odd(z)
even_odd_1(z)
wrapper()(z)


"""
Введите число: 569
Количество четных чисел: 1, нечетных цифр: 2

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.6 MiB     19.6 MiB           1   @profile
    12                                         def even_odd(numeric, even=0, odd=0):
    13     19.6 MiB      0.0 MiB           1       if numeric == 0:
    14     19.6 MiB      0.0 MiB           1           print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    15                                             else:
    16                                                 if (numeric % 10) % 2 == 0:
    17                                                     even += 1
    18                                                 else:
    19                                                     odd += 1
    20                                                 return even_odd(numeric // 10, even, odd)



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.6 MiB     19.6 MiB           2   @profile
    12                                         def even_odd(numeric, even=0, odd=0):
    13     19.6 MiB      0.0 MiB           2       if numeric == 0:
    14     19.6 MiB      0.0 MiB           1           print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    15                                             else:
    16     19.6 MiB      0.0 MiB           1           if (numeric % 10) % 2 == 0:
    17                                                     even += 1
    18                                                 else:
    19     19.6 MiB      0.0 MiB           1               odd += 1
    20     19.6 MiB      0.0 MiB           1           return even_odd(numeric // 10, even, odd)



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.6 MiB     19.6 MiB           3   @profile
    12                                         def even_odd(numeric, even=0, odd=0):
    13     19.6 MiB      0.0 MiB           3       if numeric == 0:
    14     19.6 MiB      0.0 MiB           1           print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    15                                             else:
    16     19.6 MiB      0.0 MiB           2           if (numeric % 10) % 2 == 0:
    17     19.6 MiB      0.0 MiB           1               even += 1
    18                                                 else:
    19     19.6 MiB      0.0 MiB           1               odd += 1
    20     19.6 MiB      0.0 MiB           2           return even_odd(numeric // 10, even, odd)



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.6 MiB     19.6 MiB           4   @profile
    12                                         def even_odd(numeric, even=0, odd=0):
    13     19.6 MiB      0.0 MiB           4       if numeric == 0:
    14     19.6 MiB      0.0 MiB           1           print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    15                                             else:
    16     19.6 MiB      0.0 MiB           3           if (numeric % 10) % 2 == 0:
    17     19.6 MiB      0.0 MiB           1               even += 1
    18                                                 else:
    19     19.6 MiB      0.0 MiB           2               odd += 1
    20     19.6 MiB      0.0 MiB           3           return even_odd(numeric // 10, even, odd)


Количество четных чисел: 1, нечетных цифр: 2

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    23     19.6 MiB     19.6 MiB           1   @profile
    24                                         def even_odd_1(numeric, even=0, odd=0):
    25     19.6 MiB      0.0 MiB           4       while numeric != 0:
    26     19.6 MiB      0.0 MiB           3           if (numeric % 10) % 2 == 0:
    27     19.6 MiB      0.0 MiB           1               even += 1
    28                                                 else:
    29     19.6 MiB      0.0 MiB           2               odd += 1
    30     19.6 MiB      0.0 MiB           3           numeric = numeric // 10
    31                                             else:
    32     19.6 MiB      0.0 MiB           1           print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35     19.6 MiB     19.6 MiB           1   @profile
    36                                         def wrapper():
    37     19.6 MiB      0.0 MiB           1       def even_odd_3(numeric, even=0, odd=0):
    38                                                 if numeric == 0:
    39                                                     return print(f'Количество четных чисел: {even}, нечетных цифр: {odd}')
    40                                                 else:
    41                                                     if (numeric % 10) % 2 == 0:
    42                                                         even += 1
    43                                                     else:
    44                                                         odd += 1
    45                                                     return even_odd_3(numeric // 10, even, odd)
    46     19.6 MiB      0.0 MiB           1       return even_odd_3


Количество четных чисел: 1, нечетных цифр: 2
"""

"""
При профилированиии пямять с рекурсией, возникла проблема в том что при 
введеном, исходном трехзначном числе замеры памяти производились 4 раза, а 
когда я поменял рекурсию на цикл, проводился только один замер. Чтобы в примере 
с рекурсией сделать один замер, нужно функцию обернуть в функцию.
"""
