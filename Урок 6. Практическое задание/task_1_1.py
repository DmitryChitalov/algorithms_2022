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
# четвертое задание второго дз с курса алгоритм


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res

    return wrapper


@decor
def func_sum_n(x, i=0, res=0, num=1):
    if x != i:
        res += num
        num /= -2
        i += 1
        return func_sum_n(x, i, res, num)
    if x == i:
        return res


@decor
def func_sum_2(count, start=1, result=0):
    while count > 0:
        result += start
        count -= 1
        start /= -2
    else:
        return result


# func_sum_n(100)
# 0.25
# print('\n')
print(func_sum_2(100))
# 0.01171875
"""
цикл использует меньше памяти чем рекурсия, поэтому и применил цикл
рекурсия использует стек для хранения вызовов, поэтому она ест больше памяти
"""

