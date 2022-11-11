"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""

"""Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 +5+9=28– делится нацело на 7.
Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7."""


# Изначальная версия
from memory_profiler import profile


@profile
def cub_sum():
    cub_list = []

    for i in range(1000):
        if i % 2 != 0:
            cub_list.append(i ** 3)

    # function for digit sum of number
    def sum_num_list(number):
        # convert number to string and create list
        a = str(number)
        b = []
        for j in a:
            b.append(j)
        # convert list of strings to digits
        c = []
        for j in b:
            j = int(j)
            c.append(j)
        # make sum of all digits from list
        result = 0
        for n in c:
            result += n

        return result

    # using sum_num_list() create list of sums
    cub_list1 = []
    for i in cub_list:
        cub_list1.append(sum_num_list(i))

    # create list with //7 numbers
    cub_list2 = []
    for i in cub_list1:
        if i % 7 == 0:
            cub_list2.append(i)

    # using only arithmetics calculate sum of cub_list2
    result1 = 0
    for i in cub_list2:
        result1 += i

    # add 17 to each element of the list
    cub_list3 = []
    for i in cub_list2:
        cub_list3.append(i + 17)

    # calculate same sum as above
    cub_list4 = []
    for i in cub_list3:
        cub_list4.append(sum_num_list(i))

    cub_list5 = []
    for i in cub_list4:
        if i % 7 == 0:
            cub_list5.append(i)

    return result1, sum(cub_list5)


print(cub_sum())


# Оптимизированная версия
from memory_profiler import profile


@profile
def cub_sum():
    cub_list = (i ** 3 for i in range(1000) if i % 2 != 0)

    def sum_num_list(number):
        return sum([int(i) for i in str(number)])

    cub_list1 = [i for i in [sum_num_list(i) for i in cub_list] if i % 7 == 0]

    cub_list2 = [i for i in [sum_num_list(i) for i in [(i + 17) for i in cub_list1]] if i % 7 == 0]

    return sum(cub_list1), sum(cub_list2)


print(cub_sum())

"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     18.7 MiB     18.7 MiB           1   @profile
    14                                         def cub_sum():
    15     18.7 MiB      0.0 MiB           1       cub_list = []
    16                                         
    17     18.7 MiB      0.0 MiB        1001       for i in range(1000):
    18     18.7 MiB      0.0 MiB        1000           if i % 2 != 0:
    19     18.7 MiB      0.0 MiB         500               cub_list.append(i ** 3)
    20                                         
    21                                             # function for digit sum of number
    22     18.7 MiB      0.0 MiB         607       def sum_num_list(number):
    23                                                 # convert number to string and create list
    24     18.7 MiB      0.0 MiB         606           a = str(number)
    25     18.7 MiB      0.0 MiB         606           b = []
    26     18.7 MiB      0.0 MiB        4886           for j in a:
    27     18.7 MiB      0.0 MiB        4280               b.append(j)
    28                                                 # convert list of strings to digits
    29     18.7 MiB      0.0 MiB         606           c = []
    30     18.7 MiB      0.0 MiB        4886           for j in b:
    31     18.7 MiB      0.0 MiB        4280               j = int(j)
    32     18.7 MiB      0.0 MiB        4280               c.append(j)
    33                                                 # make sum of all digits from list
    34     18.7 MiB      0.0 MiB         606           result = 0
    35     18.7 MiB      0.0 MiB        4886           for n in c:
    36     18.7 MiB      0.0 MiB        4280               result += n
    37                                         
    38     18.7 MiB      0.0 MiB         606           return result
    39                                         
    40                                             # using sum_num_list() create list of sums
    41     18.7 MiB      0.0 MiB           1       cub_list1 = []
    42     18.7 MiB      0.0 MiB         501       for i in cub_list:
    43     18.7 MiB      0.0 MiB         500           cub_list1.append(sum_num_list(i))
    44                                         
    45                                             # create list with //7 numbers
    46     18.7 MiB      0.0 MiB           1       cub_list2 = []
    47     18.7 MiB      0.0 MiB         501       for i in cub_list1:
    48     18.7 MiB      0.0 MiB         500           if i % 7 == 0:
    49     18.7 MiB      0.0 MiB         106               cub_list2.append(i)
    50                                         
    51                                             # using only arithmetics calculate sum of cub_list2
    52     18.7 MiB      0.0 MiB           1       result1 = 0
    53     18.7 MiB      0.0 MiB         107       for i in cub_list2:
    54     18.7 MiB      0.0 MiB         106           result1 += i
    55                                         
    56                                             # add 17 to each element of the list
    57     18.7 MiB      0.0 MiB           1       cub_list3 = []
    58     18.7 MiB      0.0 MiB         107       for i in cub_list2:
    59     18.7 MiB      0.0 MiB         106           cub_list3.append(i + 17)
    60                                         
    61                                             # calculate same sum as above
    62     18.7 MiB      0.0 MiB           1       cub_list4 = []
    63     18.7 MiB      0.0 MiB         107       for i in cub_list3:
    64     18.7 MiB      0.0 MiB         106           cub_list4.append(sum_num_list(i))
    65                                         
    66     18.7 MiB      0.0 MiB           1       cub_list5 = []
    67     18.7 MiB      0.0 MiB         107       for i in cub_list4:
    68     18.7 MiB      0.0 MiB         106           if i % 7 == 0:
    69     18.7 MiB      0.0 MiB          62               cub_list5.append(i)
    70                                         
    71     18.7 MiB      0.0 MiB           1       return result1, sum(cub_list5)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     18.4 MiB     18.4 MiB           1   @profile
    14                                         def cub_sum():
    15     18.4 MiB      0.0 MiB        1503       cub_list = (i ** 3 for i in range(1000) if i % 2 != 0)
    16                                         
    17     18.4 MiB      0.0 MiB         607       def sum_num_list(number):
    18     18.4 MiB      0.0 MiB        6098           return sum([int(i) for i in str(number)])
    19                                         
    20     18.4 MiB      0.0 MiB        1005       cub_list1 = [i for i in [sum_num_list(i) for i in cub_list] if i % 7 == 0]
    21                                         
    22     18.4 MiB      0.0 MiB         325       cub_list2 = [i for i in [sum_num_list(i) for i in [(i + 17) for i in cub_list1]] if i % 7 == 0]
    23                                         
    24     18.4 MiB      0.0 MiB           1       return sum(cub_list1), sum(cub_list2)

    Удалось добиться небольшой оптимизации кода"""




