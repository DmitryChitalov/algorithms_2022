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


# Доработанная задача № 2 из 1 урока по курсу "Основы Python"
from memory_profiler import profile


# ИСХОДНОЕ
@profile
def task_1_2():
    cube_list = []
    sum_list = 0

    for i in range(0, 50000):
        if i % 2 != 0:
            cube_list.append(i ** 3)

    for element in cube_list:
        sum_elements = 0
        cycle_element = element
        while cycle_element / 10 > 0:
            sum_elements += cycle_element % 10
            cycle_element = cycle_element // 10
        if sum_elements % 7 == 0:
            sum_list += element

    print(sum_list)


# ОПТИМИЗИРОВАННОЕ
@profile
def task_1_2_optimize():
    sum_list = 0
    cube_list = map(lambda x: x**3, filter(lambda x: x % 2 != 0, range(0, 50000)))

    for element in cube_list:
        sum_elements = 0
        cycle_element = element
        while cycle_element / 10 > 0:
            sum_elements += cycle_element % 10
            cycle_element = cycle_element // 10
        if sum_elements % 7 == 0:
            sum_list += element

    print(sum_list)


task_1_2()
task_1_2_optimize()


"""
Filename: D:/study/gb/gb_alg/git/algorithms_2022/Урок 6. Практическое задание/task_1_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38     26.6 MiB     26.6 MiB           1   @profile
    39                                         def task_1_2():
    40     26.6 MiB      0.0 MiB           1       cube_list = []
    41     26.6 MiB      0.0 MiB           1       sum_list = 0
    42                                         
    43     27.6 MiB   -482.7 MiB       50001       for i in range(0, 50000):
    44     27.6 MiB   -483.2 MiB       50000           if i % 2 != 0:
    45     27.6 MiB   -241.0 MiB       25000               cube_list.append(i ** 3)
    46                                         
    47     27.6 MiB   -731.6 MiB       25001       for element in cube_list:
    48     27.6 MiB   -731.5 MiB       25000           sum_elements = 0
    49     27.6 MiB   -731.5 MiB       25000           cycle_element = element
    50     27.6 MiB -11039.0 MiB      356690           while cycle_element / 10 > 0:
    51     27.6 MiB -10307.4 MiB      331690               sum_elements += cycle_element % 10
    52     27.6 MiB -10307.4 MiB      331690               cycle_element = cycle_element // 10
    53     27.6 MiB   -731.6 MiB       25000           if sum_elements % 7 == 0:
    54     27.6 MiB    -87.4 MiB        2978               sum_list += element
    55                                         
    56     27.5 MiB     -0.1 MiB           1       print(sum_list)



Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    59     27.1 MiB     27.1 MiB           1   @profile
    60                                         def task_1_2_optimize():
    61     27.1 MiB      0.0 MiB           1       sum_list = 0
    62     27.1 MiB -29277.5 MiB      150001       cube_list = map(lambda x: x**3, filter(lambda x: x % 2 != 0, 
    range(0, 50000)))
    63                                         
    64     27.1 MiB  -4879.8 MiB       25001       for element in cube_list:
    65     27.1 MiB  -4879.6 MiB       25000           sum_elements = 0
    66     27.1 MiB  -4879.6 MiB       25000           cycle_element = element
    67     27.1 MiB -72693.8 MiB      356690           while cycle_element / 10 > 0:
    68     27.1 MiB -69099.4 MiB      331690               sum_elements += cycle_element % 10
    69     27.1 MiB -67814.2 MiB      331690               cycle_element = cycle_element // 10
    70     27.1 MiB  -5168.7 MiB       25000           if sum_elements % 7 == 0:
    71     27.1 MiB   -572.5 MiB        2978               sum_list += element
    72                                         
    73     26.9 MiB     -0.2 MiB           1       print(sum_list)
    
Выводы: 
Замена цикла на связку map+filter+lambda даёт небольшую экономию по занимаемой памяти
"""