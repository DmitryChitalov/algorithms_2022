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
from memory_profiler import profile
from pympler import asizeof
from json import loads, dumps


# Функция с урока 3, задание 1, курс Алгоритмы
@profile
def complete_dict(user_dict):
    for element in range(1, 100000):  # O(1)
        user_dict[element] = element ** 2  # O(1)
    return user_dict


my_dict = {}
complete_dict(my_dict)
print('Размер dict: ', asizeof.asizeof(complete_dict(my_dict)))

"""
Размер dict:  11 642 392

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    39     20.8 MiB     20.8 MiB           1   @profile
    40                                         def complete_dict(user_dict):
    41     31.9 MiB      6.1 MiB      100000       for element in range(1, 100000):  # O(1)
    42     31.9 MiB      5.0 MiB       99999           user_dict[element] = element ** 2  # O(1)
    43     31.9 MiB      0.0 MiB           1       return user_dict
"""

"""
Для оптимизации использования памяти - выполним сериализацию словаря в формат json-строк
"""


@profile
def complete_dict(user_dict):
    for element in range(1, 100000):  # O(1)
        user_dict[element] = element ** 2  # O(1)
    dumped_dict = dumps(user_dict)
    return dumped_dict


complete_dict(my_dict)

print('Размер json: ', asizeof.asizeof(complete_dict(my_dict)))

"""
Размер json:  2 042 688

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    63     33.3 MiB     33.3 MiB           1   @profile
    64                                         def complete_dict(user_dict):
    65     33.3 MiB      0.0 MiB      100000       for element in range(1, 100000):  # O(1)
    66     33.3 MiB      0.0 MiB       99999           user_dict[element] = element ** 2  # O(1)
    67     37.2 MiB      3.9 MiB           1       dumped_dict = dumps(user_dict)
    68     37.2 MiB      0.0 MiB           1       return dumped_dict
"""

"""
Заполнение словаря при помощи оптимизированной функции complete_dict
расходует немного больше памяти, но сам словарь занимает значительно меньше места
"""
