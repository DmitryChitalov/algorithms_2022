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

Это файл для первого скрипта
"""
# Задание №3 из урока 1
from memory_profiler import profile
from collections import namedtuple


@profile
def top3_1():
    data = {'Gazprom': 20000, 'Sberbank': 15000, 'Yandex': 12000, 'Lukoil': 17500, 'MVideo': 7000, 'FIVE': 12000}
    dict_to_sort = data.copy()
    new_dict = {}
    for i in range(3):
        lst = [(k, v) for k, v in dict_to_sort.items()]
        maxi = lst[0]
        for j in range(len(lst)-1):
            if maxi[1] < lst[j+1][1]:
                maxi = lst[j+1]
        new_dict[maxi[0]] = maxi[1]
        del dict_to_sort[maxi[0]]
    return new_dict


@profile
def top3_2():
    company = namedtuple('company',('x y'))
    companies = (company(x='Gazprom', y=20000), company(x='Sberbank', y=15000),company(x='Yandex', y=12000), company(x='Lukoil', y=17500), company(x='MVideo', y=7000), company(x='FIVE', y=12000))
    new_dict = {}
    for _ in range(3):
        lst = [(k, v) for k, v in companies.items()]
        maxi = lst[0]
        for j in range(len(lst) - 1):
            if maxi[1] < lst[j + 1][1]:
                maxi = lst[j + 1]
        new_dict[maxi[0]] = maxi[1]
        del lst[maxi[0]]
    del lst
    return new_dict


top3_1()
top3_2()


# Изменил способ хранения данных со словаря на namedtuple