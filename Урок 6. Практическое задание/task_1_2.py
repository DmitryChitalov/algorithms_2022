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


Python-basic - https://github.com/Frvzr/gb_python_basics/blob/master/Koposhilov_Ivan_dz_5/task_5_4.py

Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
"""

from time import perf_counter
import sys
from memory_profiler import profile, memory_usage
from random import randint


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


@profile
def get_numbers_1(src: list):
    """
    Генератор, выводящий значения из списка, которые больше предыдущего значения
    :src: list с значениями
    :return: generator
    """

    start = perf_counter()
    result = []
    for i in range(0, len(src) - 1):
        if src[i] < src[i + 1]:
            result.append(src[i + 1])
    print(sys.getsizeof(result), perf_counter() - start)  # 120 0.0000165
    return result


@profile
def get_numbers_2(src: list):
    start = perf_counter()
    result = (src[i + 1]
              for i in range(0, len(src) - 1) if src[i] < src[i + 1])
    print(sys.getsizeof(result), perf_counter() - start)  # 112 0.0000075
    return result


# Оптимизированный вариант
@decor
def get_numbers_3(src: list):
    """
    Генератор
    """
    for num in src:
        if src[num] < src[num + 1]:
            yield num


src = [randint(1, 100000) for _ in range(1, 1000000)]
if __name__ == "__main__":
    generator, mem_diff = get_numbers_3(src)
    start = perf_counter()
    for num in generator:
        print(num, end=' ')
    print(perf_counter() - start)
    print(f'\nВыполнение заняло {mem_diff} Mib')
    get_numbers_1(src)
    get_numbers_2(src)


"""
Задание было оптимизированно генератором, LC увеличивает скорость

Выполнение заняло 0.0078125 Mib
4167352 39.1552479
Filename: c:\Users\user\Desktop\test1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   124     58.5 MiB     58.5 MiB           1   @profile
   125                                         def get_numbers_1(src: list):       
   132     58.5 MiB      0.0 MiB           1       start = perf_counter()
   133     58.5 MiB      0.0 MiB           1       result = []
   134     62.7 MiB -11119.7 MiB      999999       for i in range(0, len(src) - 1):
   135     62.7 MiB -11119.7 MiB      999998           if src[i] < src[i + 1]:
   136     62.7 MiB  -5554.7 MiB      499885               result.append(src[i + 1])
   137     62.7 MiB      0.0 MiB           1       print(sys.getsizeof(result), perf_counter() - start)  # 120 0.0000165
   138     62.7 MiB      0.0 MiB           1       return result


112 7.959999999940237e-05
Filename: c:\Users\user\Desktop\test1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   141     58.5 MiB     58.5 MiB           1   @profile
   142                                         def get_numbers_2(src: list):
   143     58.5 MiB      0.0 MiB           1       start = perf_counter()
   144     58.5 MiB      0.0 MiB           2       result = (src[i + 1]
   145     58.5 MiB      0.0 MiB           1                 for i in range(0, len(src) - 1) if src[i] < src[i + 1])
   146     58.5 MiB      0.0 MiB           1       print(sys.getsizeof(result), perf_counter() - start)  # 112 0.0000075
   147     58.5 MiB      0.0 MiB           1       return result

"""
