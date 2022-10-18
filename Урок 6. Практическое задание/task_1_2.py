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

Это файл для второго скрипта
"""

"""
В качестве примера выбрана 2 задача из 1 урока по Основам python
"""


from memory_profiler import profile
from numpy import array

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
    cube_list = array([i ** 3 for i in range(0, 50000) if i % 2 != 0])

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
94743520095335132
Filename: /home/fox/Рабочий стол/algorithms_2022/Урок 6. Практическое задание/task_1_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     35.5 MiB     35.5 MiB           1   @profile
    43                                         def task_1_2():
    44     35.5 MiB      0.0 MiB           1       cube_list = []
    45     35.5 MiB      0.0 MiB           1       sum_list = 0
    46                                         
    47     36.5 MiB      0.3 MiB       50001       for i in range(0, 50000):
    48     36.5 MiB      0.0 MiB       50000           if i % 2 != 0:
    49     36.5 MiB      0.8 MiB       25000               cube_list.append(i ** 3)
    50                                         
    51     36.5 MiB      0.0 MiB       25001       for element in cube_list:
    52     36.5 MiB      0.0 MiB       25000           sum_elements = 0
    53     36.5 MiB      0.0 MiB       25000           cycle_element = element
    54     36.5 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    55     36.5 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    56     36.5 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    57     36.5 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    58     36.5 MiB      0.0 MiB        2978               sum_list += element
    59                                         
    60     36.5 MiB      0.0 MiB           1       print(sum_list)


94743520095335132
Filename: /home/fox/Рабочий стол/algorithms_2022/Урок 6. Практическое задание/task_1_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    63     36.5 MiB     36.5 MiB           1   @profile
    64                                         def task_1_2_optimize():
    65     36.5 MiB      0.0 MiB           1       sum_list = 0
    66     36.8 MiB      0.3 MiB       50003       cube_list = array([i ** 3 for i in range(0, 50000) if i % 2 != 0])
    67                                         
    68     36.8 MiB      0.0 MiB       25001       for element in cube_list:
    69     36.8 MiB      0.0 MiB       25000           sum_elements = 0
    70     36.8 MiB      0.0 MiB       25000           cycle_element = element
    71     36.8 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    72     36.8 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    73     36.8 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    74     36.8 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    75     36.8 MiB      0.0 MiB        2978               sum_list += element
    76                                         
    77     36.8 MiB      0.0 MiB           1       print(sum_list)

Cпискок заменил на numpy.ndarray.
Как показывают замеры экономия памяти составила 1.3 MiB
"""