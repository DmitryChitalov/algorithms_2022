"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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
"до оптимизации "
from memory_profiler import profile, memory_usage
from sys import getsizeof
from sys import getsizeof
from time import perf_counter
from collections import defaultdict

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
################################ try del elem which duble in list #########################3

def decor_memory(func):
    def wrapper():
        memory_1 = memory_usage()
        res = func()
        memory_2 = memory_usage()
        all_memory = memory_1[0] - memory_2[0]
        return res, print(all_memory)

    return wrapper


@decor_memory
def old_code():
    empty_list = []
    for i in range(len(src)):
        if src.count(src[i]) <= 1:
            empty_list.append(src[i])
    return empty_list

print(old_code(), getsizeof(old_code))      # -0.00390625/136
"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    54     18.2 MiB     18.2 MiB           1   @profile
    55                                         def old_code():
    56     18.2 MiB      0.0 MiB           1       empty_list = []
    57     18.2 MiB      0.0 MiB          15       for i in range(len(src)):
    58     18.2 MiB      0.0 MiB          14           if src.count(src[i]) <= 1:
    59     18.2 MiB      0.0 MiB           6               empty_list.append(src[i])"""

# print(getsizeof(empty_list))
# [23, 1, 3, 10, 4, 11] 2.010000000000206e-05
# 68
@decor_memory
def full_dict():
    some_dict = dict()
    for i in src:
        if src.count(i) < 2:
            some_dict.setdefault(i)
    return some_dict


print(full_dict(), getsizeof(full_dict))        # 0.0/136

"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     18.3 MiB     18.3 MiB           1   @profile
    69                                         def full_dict():
    70     18.3 MiB      0.0 MiB           1       some_dict = dict()
    71     18.3 MiB      0.0 MiB          15       for i in src:
    72     18.3 MiB      0.0 MiB          14           if src.count(i) < 2:
    73     18.3 MiB      0.0 MiB           6               some_dict.setdefault(i)
    74     18.3 MiB      0.0 MiB           1       return some_dict"""

