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

Это файл для пятого скрипта
"""
from memory_profiler import profile
from random  import randint

@profile
def reverse_num_profiled(number):

    def reverse_num(number):
        if number // 10 == 0:
            return str(number)
        else:
            return str(number % 10) + str(reverse_num(number // 10))
    return reverse_num(number)

@profile
def reverse_num2(number):
    string = str(number)
    reverse_string = ''
    for i in range(len(string)):
        reverse_string = reverse_string + string[len(string)-i-1]


    return reverse_string

num = randint(10**800, 10**900)
print(reverse_num_profiled(num))
"""Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     15.1 MiB     15.1 MiB           1   @profile
    37                                         def reverse_num_profiled(number):
    38                                         
    39     16.6 MiB      1.3 MiB         901       def reverse_num(number):
    40     16.6 MiB      0.1 MiB         900           if number // 10 == 0:
    41     16.6 MiB      0.0 MiB           1               return str(number)
    42                                                 else:
    43     16.6 MiB      0.0 MiB         899               return str(number % 10) + str(reverse_num(number // 10))
    44     16.6 MiB      0.0 MiB           1       return reverse_num(number)
"""

print(reverse_num2(num))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    46     16.6 MiB     16.6 MiB           1   @profile
    47                                         def reverse_num2(number):
    48     16.6 MiB      0.0 MiB           1       string = str(number)
    49     16.6 MiB      0.0 MiB           1       reverse_string = ''
    50     16.6 MiB      0.0 MiB         901       for i in range(len(string)):
    51     16.6 MiB      0.0 MiB         900           reverse_string = reverse_string + string[len(string)-i-1]
    52                                         
    53                                         
    54     16.6 MiB      0.0 MiB           1       return reverse_string

При замене рекурсивной функции на простой цикл, уменьшение использования памяти не происходит

"""


