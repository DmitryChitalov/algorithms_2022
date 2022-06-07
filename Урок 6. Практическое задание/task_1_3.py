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
# from random import randint, choice
from memory_profiler import profile
# from collections import Counter
import random

# Заполнение массива тестовыми данными
company_storage = []
for x in range(4000):
    company_storage.append({
        'name': ''.join(random.choice('vxnxikmhdc') for i in range(32)),
        'income': random.randint(893945, 93277238)
    })

# Arrays
@profile
def first_method(in_storage):
    gen_new_list = []
    for idx, x in enumerate(in_storage):
        gen_new_list.append((x['income'], idx))
    gen_new_list.sort(reverse=True)
    return [in_storage[i] for i in map(lambda x: x[1], gen_new_list[:3])]

#################################

def find_max(data, count):
    excluded = set()
    for x in range(0, count):
        max = 0
        slot = 0
        for idx, x in enumerate(data):
            if max <= x['income'] and idx not in excluded:
                slot = idx
                max = x['income']
        excluded.add(slot)
        yield data[slot]

# Generator
@profile
def two_method(in_storage: list) -> list:
    return list(find_max(in_storage, 3))

print(f"first_method: {first_method(company_storage)}")
print(f"two_method: {two_method(company_storage)}")

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    46     20.9 MiB     20.9 MiB           1   @profile
    47                                         def first_method(in_storage):
    48     20.9 MiB      0.0 MiB           1       gen_new_list = []
    49     21.2 MiB      0.2 MiB        4001       for idx, x in enumerate(in_storage):
    50     21.2 MiB      0.2 MiB        4000           gen_new_list.append((x['income'], idx))
    51     21.2 MiB      0.0 MiB           1       gen_new_list.sort(reverse=True)
    52     21.2 MiB      0.0 MiB          12       return [in_storage[i] for i in map(lambda x: x[1], gen_new_list[:3])]


first_method: [
{'name': 'iixxiknmmvmnddvnhdxhvxhxvnvmxhmh', 'income': 92931775}, 
{'name': 'xmkhnmicxnhxcnmhxxhvdhdcvkxddxdh', 'income': 91841551}, 
{'name': 'xkxxxxnmhvkxmmikhmckxdivcvcknnxh', 'income': 83190375}
]

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    69     21.3 MiB     21.3 MiB           1   @profile
    70                                         def two_method(in_storage: list) -> list:
    71     21.3 MiB      0.0 MiB           1       return list(find_max(in_storage, 3))


two_method: [
{'name': 'iixxiknmmvmnddvnhdxhvxhxvnvmxhmh', 'income': 92931775}, 
{'name': 'xmkhnmicxnhxcnmhxxhvdhdcvkxddxdh', 'income': 91841551}, 
{'name': 'xkxxxxnmhvkxmmikhmckxdivcvcknnxh', 'income': 83190375}
]

    Аналитика:
        Заменили стандартный цикл на генератор, он позволяет уменьшить потребляемое кол-во памяти
        Причём сделали так, чтобы в самом генераторе формировалось нужное нам кол-во максимальных по 
        доходу компаний
"""