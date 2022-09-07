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
# Исходный код: Урок 4. Практическое задание task_1.py
#
# Способ 1 минимизации расходования памяти. Ленивые вычисления
#
from memory_profiler import memory_usage
# MEBIBYTE = 1048576
test_arr = [n for n in range(10000)]


def decor_memory_usage(func):
    def wrapper(*args, **kwargs):
        mem1 = memory_usage()
        res = func(args[0], **kwargs)
        mem2 = memory_usage()
        mem_diff = mem2[0] - mem1[0]
        return res, mem_diff
    return wrapper


@decor_memory_usage  # 1 Mebibyte = 1048576 Bytes
def func_1(nums):
    new_arr = []
    for num in range(len(nums)):
        if num % 2 == 0:
            new_arr.append(num)
    return new_arr


res_list_1, mem_diff_1 = func_1(test_arr)
print(f"Выполнение функции func_1 заняло {mem_diff_1:.8f} Mib")


@decor_memory_usage
def func_2(nums):
    return [num for num in nums if num % 2 == 0]


res_list_2, mem_diff_2 = func_2(test_arr)
print(f"Выполнение функции func_2 заняло {mem_diff_2:.8f} Mib")


# Модифицируем исходный код. Функция func_2 возвращает список.
# Новая функция func_3 будет возвращать итератор - generator object

@decor_memory_usage
def func_3(nums):
    for num in nums:
        if num % 2 == 0:
            yield num


res_generator_3, mem_diff_3 = func_3(test_arr)
print(f"Выполнение функции func_3 заняло {mem_diff_3:.8f} Mib")
# for i in res_generator_3:
#    print(i)
"""
Выполнение функции func_1 заняло 0.19140625 Mib
Выполнение функции func_2 заняло 0.04687500 Mib
Выполнение функции func_3 заняло 0.00000000 Mib
"""
