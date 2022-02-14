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
from memory_profiler import profile

"""-----------------------------------------------------
1.1 Для ОПТИМИЗАЦИИ используем 'Ленивые вычисления' (GE)
--------------------------------------------------------"""


# Курс 'Алгоритмы'. Вебинар2.
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...

# Мои решения
@profile
def rec_number_series_sum(num):
    def recursive_number_series_sum(count, sum_=1.0):  # Решение через рекурсию.
        if count <= 1:
            return sum_
        sum_ += recursive_number_series_sum(count - 1, -sum_ / 2)
        return sum_

    return recursive_number_series_sum(num)


@profile
def lh_number_series_sum(num):
    x = [1 / (2 ** n) * (1, -1)[n % 2 or 0] for n in range(num)]
    return sum(x)


# Мои решения, оптимизированные по памяти с использованием генератора выражений (GE)
# Заменили создание списка и шагов рекурсии длиной num на GE

@profile
def opt_number_series_sum(num):
    sum_ = 0
    for i in (1 / (2 ** n) * (1, -1)[n % 2 or 0] for n in range(num)):
        sum_ += i
    return sum_


number = 50000
rec_number_series_sum(980)
lh_number_series_sum(number)
opt_number_series_sum(number)

"""
Результаты тестов показали, что opt_number_series_sum заметно оптимизирован по памяти с помощью использования
GE (Generator Expression) вместо LC (List Comprehension) при определении числового ряда. Аналогичная рекурсивная
функция уступает обоим уже на небольших числах ряда.

Число эл-тов последовательности для рекурсивной функции - 990 (Максимум с учетом декоратора)
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    32     19.3 MiB     19.3 MiB           1   @profile
    33                                         def rec_number_series_sum(num):
    34     21.3 MiB      1.6 MiB         981       def recursive_number_series_sum(count, sum_=1.0):
    35     21.3 MiB      0.4 MiB         980           if count <= 1:
    36     21.3 MiB      0.0 MiB           1               return sum_
    37     21.3 MiB      0.0 MiB         979           sum_ += recursive_number_series_sum(count - 1, -sum_ / 2)
    38     21.3 MiB      0.0 MiB         979           return sum_
    39                                         
    40     21.3 MiB      0.0 MiB           1       return recursive_number_series_sum(num)

LC для 50000
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    43     21.3 MiB     21.3 MiB           1   @profile
    44                                         def lh_number_series_sum(num):
    45     23.7 MiB      2.4 MiB       50003       x = [1 / (2 ** n) * (1, -1)[n % 2 or 0] for n in range(num)]
    46     23.7 MiB      0.0 MiB           1       return sum(x)


GE lkz 50000
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    52     22.0 MiB     22.0 MiB           1   @profile
    53                                         def opt_number_series_sum(num):
    54     22.0 MiB      0.0 MiB           1       sum_ = 0
    55     22.2 MiB      0.2 MiB      150003       for i in (1 / (2 ** n) * (1, -1)[n % 2 or 0] for n in range(num)):
    56     22.2 MiB      0.0 MiB       50000           sum_ += i
    57     22.2 MiB      0.0 MiB           1       return sum_

"""
