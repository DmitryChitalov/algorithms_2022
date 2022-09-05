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

Это файл для третьего скрипта
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
    cube_list = tuple(i ** 3 for i in range(0, 50000) if i % 2 != 0)

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
Filename: C:\GIT\exchange\Урок 6. Практическое задание\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     19.4 MiB     19.4 MiB           1   @profile
    38                                         def task_1_2():
    39     19.4 MiB      0.0 MiB           1       cube_list = []
    40     19.4 MiB      0.0 MiB           1       sum_list = 0
    41                                         
    42     20.7 MiB      0.5 MiB       50001       for i in range(0, 50000):
    43     20.7 MiB      0.0 MiB       50000           if i % 2 != 0:
    44     20.7 MiB      0.7 MiB       25000               cube_list.append(i ** 3)
    45                                         
    46     20.7 MiB      0.0 MiB       25001       for element in cube_list:
    47     20.7 MiB      0.0 MiB       25000           sum_elements = 0
    48     20.7 MiB      0.0 MiB       25000           cycle_element = element
    49     20.7 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    50     20.7 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    51     20.7 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    52     20.7 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    53     20.7 MiB      0.0 MiB        2978               sum_list += element
    54                                         
    55     20.7 MiB      0.0 MiB           1       print(sum_list)


94743520095335132
Filename: C:\GIT\exchange\Урок 6. Практическое задание\task_1_3.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    58     20.7 MiB     20.7 MiB           1   @profile
    59                                         def task_1_2_optimize():
    60     20.7 MiB      0.0 MiB           1       sum_list = 0
    61     20.7 MiB      0.0 MiB       75003       cube_list = tuple(i ** 3 for i in range(0, 50000) if i % 2 != 0)
    62                                         
    63     20.7 MiB      0.0 MiB       25001       for element in cube_list:
    64     20.7 MiB      0.0 MiB       25000           sum_elements = 0
    65     20.7 MiB      0.0 MiB       25000           cycle_element = element
    66     20.7 MiB      0.0 MiB      356690           while cycle_element / 10 > 0:
    67     20.7 MiB      0.0 MiB      331690               sum_elements += cycle_element % 10
    68     20.7 MiB      0.0 MiB      331690               cycle_element = cycle_element // 10
    69     20.7 MiB      0.0 MiB       25000           if sum_elements % 7 == 0:
    70     20.7 MiB      0.0 MiB        2978               sum_list += element
    71                                         
    72     20.7 MiB      0.0 MiB           1       print(sum_list)



Выводы: список заменил на кортеж, как показывают замеры экономия памяти составила 1.2 MiB
"""
