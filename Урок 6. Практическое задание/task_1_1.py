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

Это файл для первого скрипта
"""
import random

from memory_profiler import profile

TEST_VALUE = random.randint(((2 ** 1000) ** 2), ((3 ** 1000) ** 2))


def test(numbers, count_even=0, count_odd=0):
    if numbers == 0:
        return count_even, count_odd
    else:
        num = numbers % 10
        numbers = numbers // 10
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    return test(numbers, count_even, count_odd)


@profile
def prof_test(num):
    return test(num)


try:
    # number = int(input('Введите число: '))
    print('Количество четных и нечетных цифр в числе равно: ' + str(prof_test(TEST_VALUE)))
except ValueError:
    print('Введено не натуральное число')


@profile
def mod_test(numbers):
    count_even = 0
    count_odd = 0
    while numbers != 0:
        num = numbers % 10
        numbers = numbers // 10
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


try:
    # number = int(input('Введите число: '))
    print('Количество четных и нечетных цифр в числе равно: ' + str(mod_test(TEST_VALUE)))
except ValueError:
    print('Введено не натуральное число')

"""
До:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52     19.2 MiB     19.2 MiB           1   @profile
    53                                         def prof_test(num):
    54     21.3 MiB      2.1 MiB           1       return test(num)
После:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    63     19.2 MiB     19.2 MiB           1   @profile
    64                                         def mod_test(numbers):
    65     19.2 MiB      0.0 MiB           1       count_even = 0
    66     19.2 MiB      0.0 MiB           1       count_odd = 0
    67     19.2 MiB      0.0 MiB         955       while numbers != 0:
    68     19.2 MiB      0.0 MiB         954           num = numbers % 10
    69     19.2 MiB      0.0 MiB         954           numbers = numbers // 10
    70     19.2 MiB      0.0 MiB         954           if num % 2 == 0:
    71     19.2 MiB      0.0 MiB         467               count_even += 1
    72                                                 else:
    73     19.2 MiB      0.0 MiB         487               count_odd += 1
    74     19.2 MiB      0.0 MiB           1       return count_even, count_odd
"""
