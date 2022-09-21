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

# Алгоритмы и структуры данных на Python. Базовый курс.
# Урок 5. Задание 3.

from memory_profiler import memory_usage
from collections import deque
import numpy


def decor_m(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение заняло {mem_diff} Mib")
        return res

    return wrapper


lst = [i for i in range(1000)]
deq_lst = deque(lst)


@decor_m
def append_lst_1(lst):
    for i in range(100000):
        lst.append(i)
    return lst


@decor_m
def append_deq_lst_1(deq_lst):
    for i in range(100000):
        deq_lst.append(i)
    return deq_lst


append_lst_1(lst)
append_deq_lst_1(deq_lst)


@decor_m
def append_lst_2(lst):
    res = numpy.array(lst)
    res_2 = numpy.append(res, res + 1)
    return res_2


@decor_m
def append_deq_lst_2(deq_lst):
    res = numpy.array(deq_lst)
    res_2 = numpy.append(res, res + 1)
    return res_2


append_lst_2(lst)
append_deq_lst_2(deq_lst)

"""
Выполнение append_lst_1 заняло 5.3203125 Mib
Выполнение append_deq_lst_1 заняло 3.0625 Mib
Выполнение append_lst_2 заняло 0.19140625 Mib
Выполнение append_deq_lst_2 заняло 0.78125 Mib
Использование модуля NumPy позволяет сильно сократить показатели затраченной памяти
"""
