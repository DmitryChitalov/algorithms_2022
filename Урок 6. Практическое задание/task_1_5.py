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

Это файл для пятого скрипта

Алгоритмы. Д/р №1, отрывок из задания №3
"""
from memory_profiler import profile


@profile
def max_profit_top3(dct):  # O(n)
    new_dct = dct.copy()  # O(n)
    top3_list = []  # O(1)
    i = 0  # O(1)
    while i < 3:  # O(1)
        top3_list.append(max(new_dct.items(), key=lambda x: x[1]))  # O(n)
        new_dct.pop(top3_list[i][0])  # O(1)
        i += 1  # O(1)
    return top3_list  # O(1)


@profile
def max_profit_top3_2(dct):  # O(n)
    new_dct = dct.copy()  # O(n)
    top3_list = []  # O(1)
    i = 0  # O(1)
    while i < 3:  # O(1)
        top3_list.append(max(new_dct.items(), key=lambda x: x[1]))  # O(n)
        new_dct.pop(top3_list[i][0])  # O(1)
        i += 1  # O(1)
    del new_dct
    return top3_list  # O(1)


dct = {i: i*2 for i in range(100000)}

max_profit_top3(dct)
max_profit_top3_2(dct)

'''
Первая функция:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     30.7 MiB     30.7 MiB           1   @profile
    49                                         def max_profit_top3(dct):  # O(n)
    50     35.7 MiB      5.0 MiB           1       new_dct = dct.copy()  # O(n)
    51     35.7 MiB      0.0 MiB           1       top3_list = []  # O(1)
    52     35.7 MiB      0.0 MiB           1       i = 0  # O(1)
    53     35.7 MiB      0.0 MiB           4       while i < 3:  # O(1)
    54     35.7 MiB      0.0 MiB      599997           top3_list.append(max(new_dct.items(),
                                                                            key=lambda x: x[1]))  # O(n)
    55     35.7 MiB      0.0 MiB           3           new_dct.pop(top3_list[i][0])  # O(1)
    56     35.7 MiB      0.0 MiB           3           i += 1  # O(1)
    57     35.7 MiB      0.0 MiB           1       return top3_list  # O(1)


Вторая функция:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    60     30.8 MiB     30.8 MiB           1   @profile
    61                                         def max_profit_top3_2(dct):  # O(n)
    62     35.8 MiB      5.0 MiB           1       new_dct = dct.copy()  # O(n)
    63     35.8 MiB      0.0 MiB           1       top3_list = []  # O(1)
    64     35.8 MiB      0.0 MiB           1       i = 0  # O(1)
    65     35.8 MiB      0.0 MiB           4       while i < 3:  # O(1)
    66     35.8 MiB      0.0 MiB      599997           top3_list.append(max(new_dct.items(),
                                                                            key=lambda x: x[1]))  # O(n)
    67     35.8 MiB      0.0 MiB           3           new_dct.pop(top3_list[i][0])  # O(1)
    68     35.8 MiB      0.0 MiB           3           i += 1  # O(1)
    69     30.8 MiB     -5.0 MiB           1       del i, new_dct
    70     30.8 MiB      0.0 MiB           1       return top3_list  # O(1)
    
Вывод: применение инструкциии del, сократило использование памяти на 5.0 MiB
'''