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
# Алгоритмы и структуры данных на Python. Базовый курс. 2.2
from memory_profiler import profile


@profile
def counting_arity(number, even=0, odd=0):
    if number == 0:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        last_number = number % 10
        if last_number % 2 == 0:
            even += 1
        else:
            odd += 1
        return counting_arity(number // 10, even, odd)


user_number = 7249901
counting_arity(user_number)

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     19.7 MiB     19.7 MiB          11   @profile
    37                                         def counting_arity(number, even=0, odd=0):
    38     19.7 MiB      0.0 MiB          11       if number == 0:
    39     19.7 MiB      0.0 MiB           1           print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    40                                             else:
    41     19.7 MiB      0.0 MiB          10           last_number = number % 10
    42     19.7 MiB      0.0 MiB          10           if last_number % 2 == 0:
    43     19.7 MiB      0.0 MiB           5               even += 1
    44                                                 else:
    45     19.7 MiB      0.0 MiB           5               odd += 1
    46     19.7 MiB      0.0 MiB          10           return counting_arity(number // 10, even, odd)
"""


@profile
def counting_arity(number, even=0, odd=0):
    while number != 0:
        last_number = number % 10
        if last_number % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number // 10
    print(f"Количество четных и нечетных цифр в числе равно: {even}, {odd}")


user_number = 7249901
counting_arity(user_number)

"""

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    69     19.7 MiB     19.7 MiB           1   @profile
    70                                         def counting_arity(number, even=0, odd=0):
    71     19.7 MiB      0.0 MiB           8       while number != 0:
    72     19.7 MiB      0.0 MiB           7           last_number = number % 10
    73     19.7 MiB      0.0 MiB           7           if last_number % 2 == 0:
    74     19.7 MiB      0.0 MiB           3               even += 1
    75                                                 else:
    76     19.7 MiB      0.0 MiB           4               odd += 1
    77     19.7 MiB      0.0 MiB           7           number = number // 10
    78     19.7 MiB      0.0 MiB           1       print(f"Количество четных и нечетных цифр в числе равно: {even}, {odd}")
"""

"""
После оптимизации функция вызывается 1 раз, но к сожалению уменьшить время работы не удалось.
В не оптимизированнном варианте после каждого вызова функции выдавалась такая таблица
"""