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
Это файл для пятого скрипта
"""

from collections import namedtuple
from recordclass import recordclass
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(mem_diff)
        return res

    return wrapper


@decor
def org_info():
    info = namedtuple('Organisation', 'name profit')
    dct = {}
    org_count = int(input('Enter number of organisations: '))
    result = {'Organisations with profit less than average: ': [],
              'Organisations with profit higher than average: ': []}
    for el in range(org_count):
        organisation = info(name=input('Enter name of organisation: '),
                            profit=sum(list(map(int, input('Enter profit per quarter sep. by space : ').split()))))
        dct[organisation.name] = organisation.profit
    avg_profit = round(sum(dct.values()) / org_count, 2)
    for key, value in dct.items():
        if value < avg_profit:
            result['Organisations with profit less than average: '].append(key)
        else:
            result['Organisations with profit higher than average: '].append(key)
    print(f'Average profit: {avg_profit}')
    for item in result.items():
        print(item)


@decor
def org_info_2():
    info = recordclass('Organisation', 'name profit')
    dct = {}
    org_count = int(input('Enter number of organisations: '))
    result = {'Organisations with profit less than average: ': [],
              'Organisations with profit higher than average: ': []}
    for el in range(org_count):
        organisation = info(name=input('Enter name of organisation: '),
                            profit=sum(list(map(int, input('Enter profit per quarter sep. by space : ').split()))))
        dct[organisation.name] = organisation.profit
    avg_profit = round(sum(dct.values()) / org_count, 2)
    for key, value in dct.items():
        if value < avg_profit:
            result['Organisations with profit less than average: '].append(key)
        else:
            result['Organisations with profit higher than average: '].append(key)
    print(f'Average profit: {avg_profit}')
    for item in result.items():
        print(item)


org_info()
org_info_2()

"""
Использование recordclass снизило потребление памяти в 3 раза
"""
