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

Это файл для третьего скрипта
"""
# Алгоритмы и структуры данных на Python. Базовый курс. 2.5
from memory_profiler import profile


@profile
def output_codes_symbols(symbol_number=32, i=1):
    if symbol_number > 127:
        return
    else:
        print(ord(chr(symbol_number)), '-', chr(symbol_number), end=' ')
        # print(f"{ord(chr(symbol_number))} - {chr(symbol_number)}", end=' ')
        if i % 10 == 0:
            print()
        return output_codes_symbols(symbol_number + 1, i + 1)


output_codes_symbols()

"""

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     20.5 MiB     20.4 MiB          97   @profile
    37                                         def output_codes_symbols(symbol_number=32, i=1):
    38     20.5 MiB      0.0 MiB          97       if symbol_number > 127:
    39     20.5 MiB      0.0 MiB           1           return
    40                                             else:
    41     20.4 MiB      0.0 MiB          96           print(ord(chr(symbol_number)), '-', chr(symbol_number), end=' ')
    42                                                 # print(f"{ord(chr(symbol_number))} - {chr(symbol_number)}", end=' ')
    43     20.4 MiB      0.0 MiB          96           if i % 10 == 0:
    44     20.4 MiB      0.0 MiB           9               print()
    45     20.5 MiB      0.0 MiB          96           return output_codes_symbols(symbol_number + 1, i + 1)
"""


@profile
def output_codes_symbols(symbol_number=32, i=1):
    while symbol_number < 128:
        print(f"{ord(chr(symbol_number))} - {chr(symbol_number)}", end=' ')
        if i % 10 == 0:
            print()
        symbol_number = symbol_number + 1
        i = i + 1


output_codes_symbols()

"""
Теперь функция output_codes_symbols вызывается однократно.
Удалось немного снизить использование памяти.
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     20.6 MiB     20.6 MiB           1   @profile
    69                                         def output_codes_symbols(symbol_number=32, i=1):
    70     20.6 MiB      0.0 MiB          97       while symbol_number < 128:
    71     20.6 MiB      0.0 MiB          96           print(f"{ord(chr(symbol_number))} - {chr(symbol_number)}", end=' ')
    72     20.6 MiB      0.0 MiB          96           if i % 10 == 0:
    73     20.6 MiB      0.0 MiB           9               print()
    74     20.6 MiB      0.0 MiB          96           symbol_number = symbol_number + 1
    75     20.6 MiB      0.0 MiB          96           i = i + 1
"""

"""
Каждый вызов рекурсивной функции выдает таблицу с замерами.
После оптимизации(замена рикурсии на цыкл while функция вызывается 1 раз.
"""