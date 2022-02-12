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

Это файл для четвертого скрипта
"""

# algorithms_Урок 5. task_2

import random
from memory_profiler import profile
from collections import namedtuple


# def main_info():
#     count = int(input('Введите количество предприятий для расчета прибыли: '))
#     company_list = []
#     Company_tuple = namedtuple('Company_tuple', ['name', 'first', 'second', 'third', 'fourth', 'annual_profit'])
#     for i in range(count):
#         company = input('Введите название предприятия: ')
#         cash = list(map(int, input('Через пробел введите прибыль данного предприятия за каждый квартал '
#                                    '(Всего 4 квартала): ').split()))
#         _ = Company_tuple(company, *cash, round(sum(cash)))
#         company_list.append(_)
#     return company_list

@profile
def analize_info(input_info):
    mean_annual_profit = sum(_.annual_profit for _ in input_info) / len(input_info)
    company_upper_mean = str([_.name for _ in input_info if _.annual_profit >= mean_annual_profit]).strip('[]')
    company_lower_mean = str([_.name for _ in input_info if _.annual_profit < mean_annual_profit]).strip('[]')
    return f'Средняя годовая прибыль всех предприятий: {mean_annual_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {company_upper_mean}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {company_lower_mean}'


@profile
def analize_info_v2(input_info):
    mean_annual_profit = sum(_.annual_profit for _ in input_info) / len(input_info)
    company_upper_mean = (_.name for _ in input_info if _.annual_profit >= mean_annual_profit)
    company_lower_mean = (_.name for _ in input_info if _.annual_profit < mean_annual_profit)
    return f'Средняя годовая прибыль всех предприятий: {mean_annual_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(company_upper_mean)}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(company_lower_mean)}'


def main_info_gen():
    company_list = []
    Company_tuple = namedtuple('Company_tuple', ['name', 'first', 'second', 'third', 'fourth', 'annual_profit'])
    for i in range(100000):
        company = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(10)))
        cash = [random.randint(0, 101) for i in range(4)]
        _ = Company_tuple(company, *cash, round(sum(cash)))
        company_list.append(_)
    return company_list


test_list = main_info_gen()

# print(analize_info(main_info()))
analize_info(test_list)
analize_info_v2(test_list)

"""
Для удобства тестирования функция для ввода данных заменена функцией для генерации данных.
В v2 lc заменён генератором и применён другой способ извлечения полученного перечня предприятий.

Результаты тестов:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    53     35.0 MiB     35.0 MiB           1   @profile
    54                                         def analize_info(input_info):
    55     35.0 MiB      0.0 MiB      200003       mean_annual_profit = sum(_.annual_profit for _ in input_info) / len(input_info)
    56     36.0 MiB      1.0 MiB      100003       company_upper_mean = str([_.name for _ in input_info if _.annual_profit >= mean_annual_profit]).strip('[]')
    57     36.7 MiB      0.7 MiB      100003       company_lower_mean = str([_.name for _ in input_info if _.annual_profit < mean_annual_profit]).strip('[]')
    58     39.3 MiB      2.6 MiB           3       return f'Средняя годовая прибыль всех предприятий: {mean_annual_profit}\n' \
    59     36.7 MiB      0.0 MiB           1              f'Предприятия, с прибылью выше среднего значения: {company_upper_mean}\n' \
    60     36.7 MiB      0.0 MiB           1              f'Предприятия, с прибылью ниже среднего значения: {company_lower_mean}'


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    63     36.1 MiB     36.1 MiB           1   @profile
    64                                         def analize_info_v2(input_info):
    65     36.1 MiB      0.0 MiB      200003       mean_annual_profit = sum(_.annual_profit for _ in input_info) / len(input_info)
    66     36.1 MiB      0.0 MiB      150256       company_upper_mean = (_.name for _ in input_info if _.annual_profit >= mean_annual_profit)
    67     36.1 MiB      0.0 MiB      149750       company_lower_mean = (_.name for _ in input_info if _.annual_profit < mean_annual_profit)
    68     38.9 MiB      2.3 MiB           3       return f'Средняя годовая прибыль всех предприятий: {mean_annual_profit}\n' \
    69     36.1 MiB      0.0 MiB           1              f'Предприятия, с прибылью выше среднего значения: {", ".join(company_upper_mean)}\n' \
    70     36.6 MiB      0.5 MiB           1              f'Предприятия, с прибылью ниже среднего значения: {", ".join(company_lower_mean)}'
"""
