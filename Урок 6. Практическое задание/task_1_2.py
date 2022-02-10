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

Это файл для второго скрипта
"""


from memory_profiler import profile


# @profile
# def func_1(nums):
#     new_arr = []
#     [new_arr.append(i) for i, el in enumerate(nums) if el % 2 == 0]
#     return new_arr[:10]
#
#
# if __name__ == '__main__':
#     print(func_1(nums=range(1, 1000000)))

#  Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     38     19.4 MiB     19.4 MiB           1   @profile
#     39                                         def func_1(nums):
#     40     19.4 MiB      0.0 MiB           1       new_arr = []
#     41     42.5 MiB -59961.1 MiB     1000002       [new_arr.append(i) for i, el in enumerate(nums) if el % 2 == 0]
#     42     38.6 MiB     -3.9 MiB           1       return new_arr[:10]


#@profile
def func_2(nums):
    new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
    print(type(new_arr))
    return (next(new_arr) for _ in range(10))


if __name__ == '__main__':
    print(type(func_2(nums=range(1, 1000000))))
    [print(el) for el in dir(filter) if el == '__next__']


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     57     19.4 MiB     19.4 MiB           1   @profile
#     58                                         def func_2(nums):
#     59     19.4 MiB      0.0 MiB          41       new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
#     60     19.4 MiB      0.0 MiB          13       return [next(new_arr) for _ in range(10)]

#  Задание 1 из урока 4 курса "Алгоритмы".
#  Немного изменен вывод на первые 10 чисел.
#  Применена функция filter для генерации массива и функция next для получения чисел из массива.
#  Результат 38.6 MiB против 19.4 MiB с использованием filter.

#  Интересный момент в описании функции https://docs.python.org/3/library/functions.html#filter
#  Note that filter(function, iterable) is equivalent to the generator expression
#  (item for item in iterable if function(item)) if function is not None and
#  (item for item in iterable if item) if function is None.
#  Поддерживает метод __next__, но при этом объект <class 'filter'>, а не <class 'generator'>.
