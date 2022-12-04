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

"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
from memory_profiler import memory_usage

user_number = 100


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# @decor
# def recur_sum(number):
#     if number == 1:
#         return number
#     else:
#         return recur_sum(number-1)[1] + number
#
#
# recur_check, mem1 = recur_sum(user_number)
# if recur_check == user_number * (user_number + 1) / 2:
#     print('Равенство верно!')
# print(mem1)
# Выполнение заняло 0.20703125 Mib

# Используем цикл
@decor
def cycle_sum(number):
        s = 0
        for num in range(1, number + 1):
            s += num
        return s


cycle_check, mem2 = cycle_sum(user_number)
if cycle_check == user_number * (user_number + 1) / 2:
    print('Равенство верно!')
print(mem2)
# Выполнение заняло 0.00390625 Mib