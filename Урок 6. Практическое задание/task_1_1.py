"""
Задание 1.

Вам нужно взять 3 любых скриптa, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.

ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 3 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке

Это файл для первого скрипта
"""

from memory_profiler import memory_usage
from random import randint
from numpy import array


def memory_info(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Не оптимизированная
@memory_info
def find_min():
    lst = [randint(1, 99) for _ in range(100000)]
    min_dig = lst[0]
    for i in lst:
        if min_dig > i:
            min_dig = i
    return min_dig


res, mem_diff = find_min()
print(mem_diff)


# Оптимизированная
@memory_info
def find_min_2():
    numpy_arr = array([randint(1, 99) for _ in range(100000)])
    yield min(numpy_arr)


res, mem_diff = find_min_2()
print(mem_diff)

"""
Сделал оптимизацию хранения элементов через numpy, использовал встроенные функции,
но максимальный эффект дал генератор

Результаты: 1 - 0.9 Mib 
            2 - 0.0 Mib
"""