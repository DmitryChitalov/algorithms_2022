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

# Алгоритмы и структуры данных на Python. Базовый курс. 3.1
from memory_profiler import profile
from pympler import asizeof
from json import loads, dumps


# Функция с урока 3, задание 1, курс Алгоритмы
@profile
def complete_dict(user_dict):
    for element in range(1, 100000):
        user_dict[element] = element ** 2
    return user_dict


my_dict = {}
complete_dict(my_dict)
print('Размер dict: ', asizeof.asizeof(complete_dict(my_dict)))

"""
Размер dict:  11642392
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    40     20.6 MiB     20.6 MiB           1   @profile
    41                                         def complete_dict(user_dict):
    42     31.5 MiB      0.0 MiB      100000       for element in range(1, 100000):  
    43     31.5 MiB     10.9 MiB       99999           user_dict[element] = element ** 2  
    44     31.5 MiB      0.0 MiB           1       return user_dict

"""

"""
Для оптимизации использования памяти - выполним сериализацию словаря в формат json-строк
"""


@profile
def complete_dict(user_dict):
    for element in range(1, 100000):
        user_dict[element] = element ** 2
    dumped_dict = dumps(user_dict)
    return dumped_dict


complete_dict(my_dict)

print('Размер json: ', asizeof.asizeof(complete_dict(my_dict)))


"""
змер json:  2042688
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     35.2 MiB     35.2 MiB           1   @profile
    69                                         def complete_dict(user_dict):
    70     35.2 MiB      0.0 MiB      100000       for element in range(1, 100000):
    71     35.2 MiB      0.0 MiB       99999           user_dict[element] = element ** 2
    72     39.1 MiB      3.9 MiB           1       dumped_dict = dumps(user_dict)
    73     39.1 MiB      0.0 MiB           1       return dumped_dict

"""

"""
После оптимизации словарь занимает меньше места
"""