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
Это файл для четвертого скрипта
"""
from memory_profiler import profile
# from memory_profiler import memory_usage
from numpy import array


# def mib_size(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_dif = m2[0] - m1[0]
#         return mem_dif, res
#
#     return wrapper


# Скрипт урока №4 задание №1 (скрипт сохраняет четные числа в новом масиве, из другого масива)
# @mib_size
@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# @mib_size
@profile
def func_1_optimize(nums):
    new_arr = array([i for i in range(len(nums)) if nums[i] % 2 == 0])
    return new_arr


if __name__ == '__main__':
    num = list(range(100000))
    print(func_1(num))
    # print(f'Выполнение заняло {mem_dif_1} Mib')
    print(func_1_optimize(num))
    # print(f'Выполнение оптимизированного скрипта заняло {mem_dif_optimize} Mib')

'''
Оптимизировал скрипт при помощи List Comprehension, а так же использовал array из библиотеки NumPy,
это позволило снизить занимаемую память.
Замер через свой декоратор:
скрипт не оптимизированный занимал 2.23046875 Mib,
оптимизированный скримпт занимает 0.59375 Mib,
Замеры провадил на одинаковых данных.

замер через @profile:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    42     34.9 MiB     34.9 MiB           1   @profile
    43                                         def func_1(nums):
    44     34.9 MiB      0.0 MiB           1       new_arr = []
    45     37.1 MiB      0.0 MiB      100001       for i in range(len(nums)):
    46     37.1 MiB      1.6 MiB      100000           if nums[i] % 2 == 0:
    47     37.1 MiB      0.7 MiB       50000               new_arr.append(i)
    48     37.1 MiB      0.0 MiB           1       return new_arr
    
Замер оптимизированного скрипта через @profile
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    51     36.4 MiB     36.4 MiB           1   @profile
    52                                         def func_1_optimize(nums):
    53     37.1 MiB      0.7 MiB      100003       new_arr = array([i for i in range(len(nums)) if nums[i] % 2 == 0])
    54     37.1 MiB      0.0 MiB           1       return new_arr
    
Тут так же видно экономия памяти на 1.6 Mib из за использования List Comprehension.
'''
