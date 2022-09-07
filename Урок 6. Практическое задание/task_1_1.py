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


"""
Python-basic - https://github.com/Frvzr/gb_python_basics/blob/master/Koposhilov_Ivan_dz_5/task_5_5.py
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""




from memory_profiler import profile, memory_usage
from random import randint
def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper

# Исходный вариант


@profile
def get_uniq_numbers(src: list):
    unique_numbers = set()
    tmp = set()
    for num in src:
        if num not in tmp:
            unique_numbers.add(num)
        else:
            unique_numbers.discard(num)
        tmp.add(num)
    result = [num for num in src if num in unique_numbers]
    return result


# @profile
# def get_uniq_numbers_2(src: list):
#     result = []
#     for num in src:
#         if src.count(num) == 1:
#             result.append(num)
#     return result


# Оптимизированный вариант

@profile
def get_uniq_numbers_1(src: list):
    """
    Добавил удаление множеств
    """
    unique_numbers = set()
    tmp = set()
    for num in src:
        if num not in tmp:
            unique_numbers.add(num)
        else:
            unique_numbers.discard(num)
        tmp.add(num)
    result = [num for num in src if num in unique_numbers]
    del tmp, unique_numbers
    return result


@decor
def get_uniq_numbers_4(src: list):
    """
    Генератор
    """
    for num in src:
        if src.count(num) == 1:
            yield num


#src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src = [randint(1, 10000) for _ in range(1, 100000)]
if __name__ == "__main__":
    print(*get_uniq_numbers(src))
    print(*get_uniq_numbers_1(src))
    # print(*get_uniq_numbers_2(src))

    generator, mem_diff = get_uniq_numbers_4(src)
    for num in generator:
        print(num, end=' ')
    print(f'\nВыполнение заняло {mem_diff} Mib')


"""
Результаты стали заметны после добавления инкрементов, при удалении временных множеств привело к экономии памяти
Так же генератор занимает всего 0.00390625 Mib

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   124     24.6 MiB     24.6 MiB           1   @profile
   125                                         def get_uniq_numbers(src: list):
   126     24.6 MiB      0.0 MiB           1       unique_numbers = set()
   127     24.6 MiB      0.0 MiB           1       tmp = set()
   128     24.8 MiB      0.0 MiB      100000       for num in src:
   129     24.8 MiB      0.0 MiB       99999           if num not in tmp:
   130     24.8 MiB      0.1 MiB       10000               unique_numbers.add(num)
   131                                                 else:
   132     24.8 MiB      0.0 MiB       89999               unique_numbers.discard(num)
   133     24.8 MiB      0.0 MiB       99999           tmp.add(num)
   134     24.8 MiB      0.0 MiB      100002       result = [num for num in src if num in unique_numbers]
   135     24.8 MiB      0.0 MiB           1       return result


5540 5203 2309 6910 3459 324 742 4889
Filename: c:\Users\user\Desktop\test1.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
   147     23.6 MiB     23.6 MiB           1   @profile
   148                                         def get_uniq_numbers_1(src: list):
   152     23.6 MiB      0.0 MiB           1       unique_numbers = set()
   153     23.6 MiB      0.0 MiB           1       tmp = set()
   154     24.5 MiB      0.0 MiB      100000       for num in src:
   155     24.5 MiB      0.0 MiB       99999           if num not in tmp:
   156     24.5 MiB      0.2 MiB       10000               unique_numbers.add(num)
   157                                                 else:
   158     24.5 MiB      0.0 MiB       89999               unique_numbers.discard(num)
   159     24.5 MiB      0.7 MiB       99999           tmp.add(num)
   160     24.5 MiB      0.0 MiB      100002       result = [num for num in src if num in unique_numbers]
   161     23.9 MiB     -0.6 MiB           1       del tmp, unique_numbers
   162     23.9 MiB      0.0 MiB           1       return result


5540 5203 2309 6910 3459 324 742 4889
5540 5203 2309 6910 3459 324 742 4889 
Выполнение заняло 0.00390625 Mib
"""
