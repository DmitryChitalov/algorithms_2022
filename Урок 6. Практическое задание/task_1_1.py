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

В качестве примера выбрана 2 вторая задача из первого урока по Основам python
"""
from memory_profiler import profile


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


@profile
def task_1_2_optimize():
    sum_list = 0
    cube_list = (i ** 3 for i in range(0, 50000) if i % 2 != 0)

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


r"""
Filename: C:\GIT\exchange\Урок 6. Практическое задание\task_1_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38     19.4 MiB     19.4 MiB           1   @profile
    39                                         def task_1_2():
    40     19.4 MiB      0.0 MiB           1       cube_list = []
    41     19.4 MiB      0.0 MiB           1       sum_list = 0
    42                                         
    43     20.8 MiB      0.5 MiB       50001       for i in range(0, 50000):
    44     20.8 MiB      0.0 MiB       50000           if i % 2 != 0:
    45     20.8 MiB      0.9 MiB       25000               cube_list.append(i ** 3)
    46                                         
    47     20.8 MiB      0.0 MiB       25001       for element in cube_list:
    48     20.8 MiB      0.0 MiB       25000           sum_elements = 0
    49     20.8 MiB      0.0 MiB       25000           cycle_element = element
    50     20.8 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    51     20.8 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    52     20.8 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    53     20.8 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    54     20.8 MiB      0.0 MiB        2978               sum_list += element
    55                                         
    56     20.8 MiB      0.0 MiB           1       print(sum_list)


94743520095335132
Filename: C:\GIT\exchange\Урок 6. Практическое задание\task_1_1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    59     20.8 MiB     20.8 MiB           1   @profile
    60                                         def task_1_2_optimize():
    61     20.8 MiB      0.0 MiB           1       sum_list = 0
    62     20.8 MiB      0.0 MiB       75003       cube_list = (i ** 3 for i in range(0, 50000) if i % 2 != 0)
    63                                         
    64     20.8 MiB      0.0 MiB       25001       for element in cube_list:
    65     20.8 MiB      0.0 MiB       25000           sum_elements = 0
    66     20.8 MiB      0.0 MiB       25000           cycle_element = element
    67     20.8 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    68     20.8 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    69     20.8 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    70     20.8 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    71     20.8 MiB      0.0 MiB        2978               sum_list += element
    72                                         
    73     20.8 MiB      0.0 MiB           1       print(sum_list)


Выводы: создание списка заменил на генератор, как показывают замеры экономия памяти составила 1.4 MiB
"""
