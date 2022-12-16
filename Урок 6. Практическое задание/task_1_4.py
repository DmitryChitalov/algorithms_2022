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

from memory_profiler import profile, memory_usage
from pympler.asizeof import asizeof


def memory(func):
    def wrapper(*args, **kwargs):
        start = memory_usage()
        my_func = func(*args)
        stop = memory_usage()
        result = stop[0] - start[0]
        return my_func, result

    return wrapper


@memory
def even_odd_count(num, even=0, odd=0):
    if num == 0:
        return print('Четных чисел:', even, 'Нечетных чисел:', odd)
    else:
        even_or_odd = num % 10
        num //= 10
        if even_or_odd % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd_count(num, even, odd)


print(asizeof(even_odd_count(4446545)))


@memory
def revers_num(num):
    even = 0
    odd = 0
    for i in range(len(str(num))):
        even_or_odd = num % 10
        num //= 10
        if even_or_odd % 2 == 0:
            even += 1
        else:
            odd += 1

    return print('Четных чисел:', even, 'Нечетных чисел:', odd)


print(asizeof(revers_num(4446545)))
'''Использовал цикл for вместо рекурсии, заняло меньше памяти 656 vs 96'''
