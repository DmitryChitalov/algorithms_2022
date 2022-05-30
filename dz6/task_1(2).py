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
from memory_profiler import profile
# from memory_profiler import memory_usage
from functools import reduce
from collections import defaultdict


# Декоратор для замера памяти скрипта
# def mib_size(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_dif = m2[0] - m1[0]
#         return mem_dif, res
#
#     return wrapper


# Скрипт урока №5 задание №2 (шестнадцатиричный калькулятор)
# @mib_size
@profile
def sum_16():
    num_1 = input('Введите первое число: ')
    num_2 = input('Введите второе число: ')
    operation = input('Выберете операцию "+" или "*": ')
    num_dict_1 = defaultdict(int)

    def split(s):
        return [char for char in s]

    num_dict_1[num_1] = int(num_1, 16)
    num_dict_1[num_2] = int(num_2, 16)
    if operation == "+":
        sum_num_1 = reduce(lambda x, y: x + y, num_dict_1.values())
        return split(hex(sum_num_1)[2:])
    elif operation == "*":
        multiply = reduce(lambda x, y: x * y, num_dict_1.values())
        return split(hex(multiply)[2:])


# Оптимизированный скрипт
# @mib_size
@profile
def sum_16_optimize():
    num_1 = input('Введите первое число: ')
    num_2 = input('Введите второе число: ')
    operation = input('Выберете операцию "+" или "*": ')
    num_dict_1 = defaultdict(int)

    def split(s):
        return [char for char in s]

    num_dict_1[num_1] = int(num_1, 16)
    num_dict_1[num_2] = int(num_2, 16)
    if operation == "+":
        sum_num_1 = reduce(lambda x, y: x + y, num_dict_1.values())
        del num_dict_1
        return split(hex(sum_num_1)[2:])
    elif operation == "*":
        multiply = reduce(lambda x, y: x * y, num_dict_1.values())
        del num_dict_1
        return split(hex(multiply)[2:])


if __name__ == '__main__':
    print(sum_16())
    print(sum_16_optimize())

''' 
Оптимизировал скрипт при помощи удаления ссылок 'del', проверил на одинаковых данных.
Замер при помощи моего декоратора @mib_size
скрипт занимал 0.0234375 Mib памяти,
после оптимизации заняло 0.0 Mib

Замер через @profile:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     19.8 MiB     19.8 MiB           1   @profile
    45                                         def sum_16():
    46     19.9 MiB      0.1 MiB           1       num_1 = input('Введите первое число: ')
    47     19.9 MiB      0.0 MiB           1       num_2 = input('Введите второе число: ')
    48     19.9 MiB      0.0 MiB           1       operation = input('Выберете операцию "+" или "*": ')
    49     19.9 MiB      0.0 MiB           1       num_dict_1 = defaultdict(int)
    50                                         
    51     19.9 MiB      0.0 MiB           2       def split(s):
    52     20.0 MiB      0.1 MiB        1298           return [char for char in s]
    
Замер оптимизарованного скрипта @profile:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    65     20.0 MiB     20.0 MiB           1   @profile
    66                                         def sum_16_optimize():
    67     19.9 MiB     -0.1 MiB           1       num_1 = input('Введите первое число: ')
    68     19.9 MiB      0.0 MiB           1       num_2 = input('Введите второе число: ')
    69     19.9 MiB      0.0 MiB           1       operation = input('Выберете операцию "+" или "*": ')
    70     19.9 MiB      0.0 MiB           1       num_dict_1 = defaultdict(int)
    71                                         
    72     19.9 MiB      0.0 MiB           2       def split(s):
    73     20.0 MiB      0.1 MiB        4334           return [char for char in s]
Так же показывает экономию памяти при удалении ссылок del.
'''
