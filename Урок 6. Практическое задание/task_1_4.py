"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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
from timeit import timeit

from memory_profiler import profile
from numpy import array

numbers_list = [4, 5, 8, 45, 9, 34, 65, 8, 12, 3, 4, 6, 78, 12312, 544, 8, 4, 5, 4, 5, 45, 4, 845, 9, 889, 1, 5, 35, 4]


@profile
def original_func():
    result = []
    for number in numbers_list:
        if numbers_list.count(number) == 1:
            result.append(number)
    return result


print(f'Время работы исходного варианта = ',
      timeit('original_func()', globals=globals(), number=1))


@profile
def array_numpy_func():
    return array(number for number in numbers_list if numbers_list.count(number) == 1)


print(f'Время работы оптимизированного оптимизированного варианта скрипта = ',
      timeit('array_numpy_func()', globals=globals(), number=1))

# numpy в разы ускоряет работу кода:
# original_func() - 0.09053338699999991
# array_numpy_func() - 0.0004316189999999942
