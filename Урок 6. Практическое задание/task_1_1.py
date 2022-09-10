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
import numpy

from memory_profiler import memory_usage
from pympler.asizeof import asizeof
from numpy import array

# Курс Основы Python lesson_1 task_2


def decor(func_1):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func_1(*args, **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Общий размер при выполнении кода: {mem_diff}')
    return wrapper


# До оптимизации
@decor
def func():
    cubes = [i ** 3 for i in range(1, 1001, 2)]
    print(f'Размер массива: {asizeof(cubes)}')
    total = 0
    sum_number = 0
    for number in cubes:
        save_number = number
        while number > 0:
            num = number % 10
            sum_number += num
            number //= 10
        if sum_number % 7 == 0:
            total += save_number
        sum_number = 0

    for i, j in enumerate(cubes):
        cubes[i] += 17

    total_1 = 0
    sum_number_1 = 0

    for number in cubes:
        save_number = number
        while number > 0:
            num = number % 10
            sum_number_1 += num
            number //= 10
        if sum_number_1 % 7 == 0:
            total_1 += save_number
        sum_number_1 = 0

    print('Сумма чисел: ', total)
    print('Сумма чисел после +17: ', total_1)


func()

# После оптимизации


@decor
def func():
    cubes = array([i ** 3 for i in range(1, 1001, 2)], dtype=numpy.float64)
    print(f'Размер массива после оптимизации: {asizeof(cubes)}')

    total = 0
    sum_number = 0

    for number in cubes:
        save_number = number
        while number > 0:
            num = number % 10
            sum_number += num
            number //= 10
        if sum_number % 7 == 0:
            total += save_number
        sum_number = 0

    for i, j in enumerate(cubes):
        cubes[i] += 17

    total_1 = 0
    sum_number_1 = 0

    for number in cubes:
        save_number = number
        while number > 0:
            num = number % 10
            sum_number_1 += num
            number //= 10
        if sum_number_1 % 7 == 0:
            total_1 += save_number
        sum_number_1 = 0

    print(f'Сумма чисел: {total}')
    print(f'Сумма чисел после +17: {total_1}')


func()

"""
Выигрываем по размеру массива при помощи NumPy(array),
и в дальнейшем по общему объёму на выполнение кода

Размер массива: 20216
Общий размер при выполнении кода: 0.05078125

Размер массива после оптимизации: 4128
Общий размер при выполнении кода: 0.0234375
"""
