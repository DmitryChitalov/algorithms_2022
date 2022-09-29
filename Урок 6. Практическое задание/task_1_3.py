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

Это файл для третьего скрипта
"""
from json import loads, dumps
from random import randint
from memory_profiler import memory_usage


def memory_decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение функции {func.__name__} заняло {mem_diff} Mib')
        return res
    return wrapper


"""
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


data_storage = {
    "Avito": 6713661,
    "Wildberries": 3671650226,
    "Ozon": 3254165,
    "Yandex": 3541066,
    "Gazprom": 682654,
    "Rosteh": 6871466,
    "Marvel": 6574416,
    "Softline": 75169159,
    "Huawei": 1489905,
    "Rostelecom": 14587125,
    "Kaspersky": 459665497,
    "Cisco Systems": 78945613,
    "Sytronics Group": 123852963,
    "Umbrella": 7418529633,
    "Tegrus": 987456321,
    "Allegro": 369852147,
    "Invent": 4561258,
    "Flowers": 32547861,
    "Olymp": 45876321,
    "WorldPress": 78254122
}


@memory_decor
def winners(data_dict):
    top_3 = {}
    data_copy = data_dict.copy()
    for _ in range(3):
        max_value = 0
        max_key = 0
        for key in data_copy.keys():
            if data_copy[key] > max_value:
                max_value = data_copy[key]
                max_key = key
        top_3[max_key] = max_value
        data_copy.pop(max_key)
    return top_3


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    71     19.3 MiB     19.3 MiB           1   @profile()
    72                                         def winners(data_dict):
    73     19.3 MiB      0.0 MiB           1       top_3 = {}
    74     19.3 MiB      0.0 MiB           1       data_copy = data_dict.copy()
    75     19.3 MiB      0.0 MiB           4       for _ in range(3):
    76     19.3 MiB      0.0 MiB           3           max_value = 0
    77     19.3 MiB      0.0 MiB           3           max_key = 0
    78     19.3 MiB      0.0 MiB          60           for key in data_copy.keys():
    79     19.3 MiB      0.0 MiB          57               if data_copy[key] > max_value:
    80     19.3 MiB      0.0 MiB          10                   max_value = data_copy[key]
    81     19.3 MiB      0.0 MiB          10                   max_key = key
    82     19.3 MiB      0.0 MiB           3           top_3[max_key] = max_value
    83     19.3 MiB      0.0 MiB           3           data_copy.pop(max_key)
    84     19.3 MiB      0.0 MiB           1       return top_3


{'Umbrella': 7418529633, 'Wildberries': 3671650226, 'Tegrus': 987456321}
"""


@memory_decor
def winners_json(data_json):
    top_3 = {}
    data_dict = loads(data_json)
    for _ in range(3):
        max_value = 0
        max_key = 0
        for key in data_dict.keys():
            if data_dict[key] > max_value:
                max_value = data_dict[key]
                max_key = key
        top_3[max_key] = max_value
        data_dict.pop(max_key)
    del data_dict
    return dumps(top_3)


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    87     19.3 MiB     19.3 MiB           1   @profile()
    88                                         def winners_json(data_json):
    89     19.3 MiB      0.0 MiB           1       top_3 = {}
    90     19.3 MiB      0.0 MiB           1       data_dict = loads(data_json)
    91     19.3 MiB      0.0 MiB           4       for _ in range(3):
    92     19.3 MiB      0.0 MiB           3           max_value = 0
    93     19.3 MiB      0.0 MiB           3           max_key = 0
    94     19.3 MiB      0.0 MiB          60           for key in data_dict.keys():
    95     19.3 MiB      0.0 MiB          57               if data_dict[key] > max_value:
    96     19.3 MiB      0.0 MiB          10                   max_value = data_dict[key]
    97     19.3 MiB      0.0 MiB          10                   max_key = key
    98     19.3 MiB      0.0 MiB           3           top_3[max_key] = max_value
    99     19.3 MiB      0.0 MiB           3           data_dict.pop(max_key)
   100     19.3 MiB      0.0 MiB           1       del data_dict
   101     19.3 MiB      0.0 MiB           1       return dumps(top_3)


{"Umbrella": 7418529633, "Wildberries": 3671650226, "Tegrus": 987456321}
"""

for i in range(1000000):
    data_storage[i] = randint(10000000, 10000000000)
data_dump = dumps(data_storage)
print(winners(data_storage))
print(winners_json(data_dump))
"""
Оптимизировали использовние памяти с помощью сериализации и удаления ссылки на словарь
"""
