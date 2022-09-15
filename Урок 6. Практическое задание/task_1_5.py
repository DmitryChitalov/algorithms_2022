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
# Алгоритмы. Урок 2. Задание 2

from memory_profiler import profile


@profile
def memory_test(number):
    def count_even_odd(num, even=0, odd=0):
        if num == 0:  # Базовый случай
            if even == 0 and odd == 0:  # Если сразу введен 0
                return 1, 0
            return even, odd

        elif num % 10 % 2:
            odd += 1
        else:
            even += 1

        return count_even_odd(num // 10, even, odd)
    return count_even_odd(number)


@profile
def memory_test_2(number):
    even = odd = 0
    for i in str(number):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


if __name__ == '__main__':
    number = 3213246543213546541321654321324654321354654132165432132465432135465413216543213246543213546541321654
    print('Количество четных и нечетных цифр в числе равно:', memory_test(number))
    print('Количество четных и нечетных цифр в числе равно:', memory_test_2(number))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    38     19.5 MiB     19.5 MiB           1   @profile
    39                                         def memory_test(number):
    40     19.7 MiB      0.3 MiB         102       def count_even_odd(num, even=0, odd=0):
    41     19.7 MiB      0.0 MiB         101           if num == 0:  # Базовый случай
    42     19.7 MiB      0.0 MiB           1               if even == 0 and odd == 0:  # Если сразу введен 0
    43                                                         return 1, 0
    44     19.7 MiB      0.0 MiB           1               return even, odd
    45                                         
    46     19.7 MiB      0.0 MiB         100           elif num % 10 % 2:
    47     19.7 MiB      0.0 MiB          52               odd += 1
    48                                                 else:
    49     19.7 MiB      0.0 MiB          48               even += 1
    50                                         
    51     19.7 MiB      0.0 MiB         100           return count_even_odd(num // 10, even, odd)
    52     19.7 MiB      0.0 MiB           1       return count_even_odd(number)

Количество четных и нечетных цифр в числе равно: (48, 52)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    55     19.7 MiB     19.7 MiB           1   @profile
    56                                         def memory_test_2(number):
    57     19.7 MiB      0.0 MiB           1       even = odd = 0
    58     19.7 MiB      0.0 MiB         101       for i in str(number):
    59     19.7 MiB      0.0 MiB         100           if int(i) % 2 == 0:
    60     19.7 MiB      0.0 MiB          48               even += 1
    61                                                 else:
    62     19.7 MiB      0.0 MiB          52               odd += 1
    63     19.7 MiB      0.0 MiB           1       return even, odd

Количество четных и нечетных цифр в числе равно: (48, 52)


Переход с рекурсии на цикл экономит память и время выполнения. 
"""