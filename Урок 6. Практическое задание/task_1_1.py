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
import random
import sys
import time
from copy import deepcopy

from memory_profiler import memory_usage
from pympler.asizeof import asizeof


def mem_decor(f):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = time.time()
        func_res = f(*args, **kwargs)
        m2 = memory_usage()
        mem = m2[0] - m1[0]
        res_time = time.time() - t1
        return f'{res_time} == {mem}'
    return wrapper

@mem_decor
def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


@mem_decor
def func_2_optimise(nums):
    new_arr = filter(lambda x: True if x % 2 == 0 else False, nums)
    return list(new_arr)


array = [random.randint(100, 1000) for _ in range(100000)]
print(func_2(array))
print(func_2_optimise(array))

