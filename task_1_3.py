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
"""

################################################################################
from memory_profiler import profile

"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
так и различаться.
"""


@profile
def func():
    a = list(range(100000))
    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]
    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")


@profile
def func_2():
    # Удаляем ненужные объекты до завершения скрипта
    a = list(range(100000))
    min_num = a[0]
    min_num2 = a[1]

    if min_num > min_num2:
        min_num, min_num2 = min_num2, min_num

    for i in range(len(a)):
        if a[i] < min_num:
            min_num2 = min_num
            min_num = a[i]
        elif a[i] < min_num2:
            min_num2 = a[i]
    del a
    print("Два наименьших элемента:", min_num, min_num2)
    print(f"Два наименьших элемента: {min_num}, {min_num2}")


func()
""" Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     19.4 MiB     19.4 MiB           1   @profile
    48                                         def func():
    49                                         
    50     23.2 MiB      3.8 MiB           1       a = list(range(100000))
    51                                         
    52     23.2 MiB      0.0 MiB           1       min_num = a[0]
    53     23.2 MiB      0.0 MiB           1       min_num2 = a[1]
    54                                         
    55     23.2 MiB      0.0 MiB           1       if min_num > min_num2:
    56                                                 min_num, min_num2 = min_num2, min_num
    57                                         
    58     23.2 MiB      0.0 MiB      100001       for i in range(len(a)):
    59     23.2 MiB      0.0 MiB      100000           if a[i] < min_num:
    60                                                     min_num2 = min_num
    61                                                     min_num = a[i]
    62     23.2 MiB      0.0 MiB      100000           elif a[i] < min_num2:
    63     23.2 MiB      0.0 MiB           1               min_num2 = a[i]
    64     23.2 MiB      0.0 MiB           1       print("Два наименьших элемента:", min_num, min_num2)
    65     23.2 MiB      0.0 MiB           1       print(f"Два наименьших элемента: {min_num}, {min_num2}")
"""

func_2()
""" Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     20.4 MiB     20.4 MiB           1   @profile
    69                                         def func_2():
    70                                         
    71     23.2 MiB      2.8 MiB           1       a = list(range(100000))
    72                                         
    73     23.2 MiB      0.0 MiB           1       min_num = a[0]
    74     23.2 MiB      0.0 MiB           1       min_num2 = a[1]
    75                                         
    76     23.2 MiB      0.0 MiB           1       if min_num > min_num2:
    77                                                 min_num, min_num2 = min_num2, min_num
    78                                         
    79     23.2 MiB      0.0 MiB      100001       for i in range(len(a)):
    80     23.2 MiB      0.0 MiB      100000           if a[i] < min_num:
    81                                                     min_num2 = min_num
    82                                                     min_num = a[i]
    83     23.2 MiB      0.0 MiB      100000           elif a[i] < min_num2:
    84     23.2 MiB      0.0 MiB           1               min_num2 = a[i]
    85     21.4 MiB     -1.8 MiB           1       del a
    86     21.4 MiB      0.0 MiB           1       print("Два наименьших элемента:", min_num, min_num2)
    87     21.4 MiB      0.0 MiB           1       print(f"Два наименьших элемента: {min_num}, {min_num2}")
"""
