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

from memory_profiler import profile


# Dz 1, task 2. Основы языка Python
# Исходный код
@profile
def my_lst_1():
    lst = [i ** 3 for i in range(1, 50000, 2)]
    final_sum_1 = 0

    def sum_digits(value):
        summ = 0
        while value != 0:
            summ += value % 10
            value //= 10
        return summ

    for i in lst:
        if sum_digits(i) % 7 == 0:
            final_sum_1 += i

    return final_sum_1


#  Оптимизированный код
@profile
def my_lst_2():
    lst = map(lambda x: x ** 3, filter(lambda x: x % 2 != 0, range(0, 50000)))
    final_sum_1 = 0

    def sum_digits(value):
        summ = 0
        while value != 0:
            summ += value % 10
            value //= 10
        return summ

    for i in lst:
        if sum_digits(i) % 7 == 0:
            final_sum_1 += i

    return final_sum_1


if __name__ == '__main__':
    my_lst_1()
    my_lst_2()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35     19.6 MiB     19.6 MiB           1   @profile
    36                                         def my_list_1():
    37     21.0 MiB      1.3 MiB       25003       lst = [i**3 for i in range(1, 50000, 2)]
    38     21.0 MiB      0.0 MiB           1       final_sum_1 = 0
    39                                         
    40     22.3 MiB      0.0 MiB       50001       def sum_digits(value):
    41     22.3 MiB      0.0 MiB       50000           summ = 0
    42     22.3 MiB      0.0 MiB      713381           while value != 0:
    43     22.3 MiB      0.0 MiB      663381               summ += value % 10
    44     22.3 MiB      0.0 MiB      663381               value //= 10
    45     22.3 MiB      0.0 MiB       50000           return summ
    46                                         
    47     21.0 MiB      0.0 MiB       25001       for i in lst:
    48     21.0 MiB      0.0 MiB       25000           if sum_digits(i) % 7 == 0:
    49     21.0 MiB      0.0 MiB        2978               final_sum_1 += i
    50     21.0 MiB      0.0 MiB           1       print(final_sum_1)
    51                                         
    52     22.3 MiB      1.3 MiB       25003       lst = [i+17 for i in lst]
    53     22.3 MiB      0.0 MiB           1       final_sum_1 = 0
    54                                         
    55     22.3 MiB      0.0 MiB       25001       for i in lst:
    56     22.3 MiB      0.0 MiB       25000           if sum_digits(i) % 7 == 0:
    57     22.3 MiB      0.0 MiB        4321               final_sum_1 += i
    58                                         
    59     22.3 MiB      0.0 MiB           1       return final_sum_1

Process finished with exit code 0


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    56     19.6 MiB     19.6 MiB           1   @profile
    57                                         def my_list_2():
    58     19.6 MiB      0.0 MiB      150001       lst = map(lambda x: x**3, filter(lambda x: x % 2 != 0, range(0, 50000)))
    59     19.6 MiB      0.0 MiB           1       final_sum_1 = 0
    60                                         
    61     19.6 MiB      0.0 MiB       25001       def sum_digits(value):
    62     19.6 MiB      0.0 MiB       25000           summ = 0
    63     19.6 MiB      0.0 MiB      356690           while value != 0:
    64     19.6 MiB      0.0 MiB      331690               summ += value % 10
    65     19.6 MiB      0.0 MiB      331690               value //= 10
    66     19.6 MiB      0.0 MiB       25000           return summ
    67                                         
    68     19.6 MiB      0.0 MiB       25001       for i in lst:
    69     19.6 MiB      0.0 MiB       25000           if sum_digits(i) % 7 == 0:
    70     19.6 MiB      0.0 MiB        2978               final_sum_1 += i
    71                                         
    72     19.6 MiB      0.0 MiB           1       return final_sum_1

"""

"""
С помощью ф-ции map мы добились уменьшения памяти.
Как мы видим вообще дополнительная память не задействуется. 
"""
