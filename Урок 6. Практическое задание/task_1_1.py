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
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...

# Рекурсия
@decor
def sum_finder_recur(number, founded_sum=0, row_element=1):
    if number > 0:
        founded_sum += row_element
        row_element /= -2
        number -= 1
        return sum_finder_recur(number, founded_sum, row_element)
    else:
        return founded_sum


# Цикл
@decor
def sum_finder_cycle(number):
    row_element = 1
    founded_sum = 0
    for i in range(number):
        founded_sum += row_element
        row_element /= -2
    return founded_sum


my_sum1, mem1 = sum_finder_recur(10**2)
print(mem1)
# Выполнение заняло 0.21875 Mib

my_sum2, mem2 = sum_finder_cycle(10**2)
print(mem2)
# Выполнение заняло 0.00390625 Mib
