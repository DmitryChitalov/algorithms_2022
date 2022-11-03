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

Это файл для четвертого скрипта
"""

from memory_profiler import profile


# Dz 2, task 2. Алгоритмы и структуры данных на Python
# Исходный код
@profile
def func_test(number):
    def even_odd_numbers(number, even_numbers=0, odd_numbers=0):
        if number == 0:
            return (f'Количество четных и нечетных цифр в числе: {even_numbers} и {odd_numbers}')
        else:
            current_number = number % 10
            if current_number % 2 == 0:
                even_numbers += 1
            else:
                odd_numbers += 1
            number //= 10
        return even_odd_numbers(number, even_numbers, odd_numbers)

    return even_odd_numbers(number)


#  Оптимизированный код
@profile
def func_test_2(number):
    even_numbers = odd_numbers = 0
    for i in str(number):
        if int(i) % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
    return (f'Количество четных и нечетных цифр в числе: {even_numbers} и {odd_numbers}')


if __name__ == '__main__':
    func_test(3213246543213546541321654321324654321354654132165432132465432135465414454532169954328813)
    func_test_2(3213246543213546541321654321324654321354654132165432132465432135465414454532169954328813)

"""
=============================================================
    37     19.3 MiB     19.3 MiB           1   @profile
    38                                         def memory_test(number):
    39     19.3 MiB      0.1 MiB          83       def even_odd_numbers(number, even_numbers=0, odd_numbers=0):
    40     19.3 MiB      0.0 MiB          82           if number == 0:
    41     19.3 MiB      0.0 MiB           1               return (f'Количество четных и нечетных цифр в числе: {even_numbers} и {odd_numbers}')
    42                                                 else:
    43     19.3 MiB      0.0 MiB          81               current_number = number % 10
    44     19.3 MiB      0.0 MiB          81               if current_number % 2 == 0:
    45     19.3 MiB      0.0 MiB          37                   even_numbers += 1
    46                                                     else:
    47     19.3 MiB      0.0 MiB          44                   odd_numbers += 1
    48     19.3 MiB      0.0 MiB          81               number //= 10
    49     19.3 MiB      0.0 MiB          81           return even_odd_numbers(number, even_numbers, odd_numbers)
    50     19.3 MiB      0.0 MiB           1       return even_odd_numbers(number)


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    54     19.2 MiB     19.2 MiB           1   @profile
    55                                         def memory_test_2(number):
    56     19.2 MiB      0.0 MiB           1       even = odd = 0
    57     19.2 MiB      0.0 MiB          82       for i in str(number):
    58     19.2 MiB      0.0 MiB          81           if int(i) % 2 == 0:
    59     19.2 MiB      0.0 MiB          37               even += 1
    60                                                 else:
    61     19.2 MiB      0.0 MiB          44               odd += 1
    62     19.2 MiB      0.0 MiB           1       return even, odd

"""

"""
Переход с рекурсии на цикл уменьшает затрачиваемую память. 
"""
