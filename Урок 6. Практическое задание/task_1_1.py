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
    data = {}
    for i in range(5000):
        name = f'Предприятие_{i}'
        income = i * 100
        data[name] = income
    new_dict = {}
    for i in range(3):
        lst = [(k, v) for k, v in data.items()]
        maxi = lst[0]
        for j in range(len(lst)-1):
            if maxi[1] < lst[j+1][1]:
                maxi = lst[j+1]
        new_dict[maxi[0]] = maxi[1]
        del data[maxi[0]]
    return new_dict


@profile
def top3_2():
    companies = []
    company = namedtuple('company','name income')
    for i in range(5000):
        name = f'Предприятие_{i}'
        income = i * 100
        companies.append(company(name=name, income=income))
    new_dict = {}
    for i in range(3):
        lst = [(name, int(income)) for name, income in companies]
        maxi = lst[0]
        for j in range(len(lst)):
            if maxi > lst[j - 1]:
                maxi = lst[j - 1]
        new_dict[i] = maxi
        del maxi
    del lst
    return new_dict


top3_1()
top3_2()


# Изменил способ хранения данных со словаря на namedtuple