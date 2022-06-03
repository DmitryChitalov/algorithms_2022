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

Алгоритмы. Д/р №5, задание №1
"""
from collections import namedtuple
from memory_profiler import memory_usage
from recordclass import recordclass


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
def func_1():
    n = 1000
    companies = namedtuple('Company', 'name quarters')
    dct = {}
    for i in range(n):
        company = companies(name=i,
                            quarters=[i, i*2, i*3, i*4])
        dct[company.name] = sum(company.quarters)
    aver_profit = round(sum(dct.values()) / n, 2)
    print(f'Средняя годовая прибыль всех предприятий: {aver_profit}')
    above_aver = []
    below_aver = []
    for k, v in dct.items():
        if v < aver_profit:
            below_aver.append(k)
        if v > aver_profit:
            above_aver.append(k)

    # print('Предприятия, с прибылью выше среднего значения: ', end='')
    # print(*above_aver, sep=', ')
    #
    # print('Предприятия, с прибылью ниже среднего значения: ', end='')
    # print(*below_aver, sep=', ')


@decor
def func_2():
    n = 1000
    companies = recordclass('Company', 'name quarters')
    dct = {}
    for i in range(n):
        company = companies(name=i,
                            quarters=[i, i*2, i*3, i*4])
        dct[company.name] = sum(company.quarters)
    aver_profit = round(sum(dct.values()) / n, 2)
    print(f'Средняя годовая прибыль всех предприятий: {aver_profit}')
    above_aver = []
    below_aver = []
    for k, v in dct.items():
        if v < aver_profit:
            below_aver.append(k)
        if v > aver_profit:
            above_aver.append(k)

    # print('Предприятия, с прибылью выше среднего значения: ', end='')
    # print(*above_aver, sep=', ')
    #
    # print('Предприятия, с прибылью ниже среднего значения: ', end='')
    # print(*below_aver, sep=', ')


func_1()  # 0.11
func_2()  # 0.03

# Использование recordclass, позволило сократить потребление памяти примерно в 3-4 раза
