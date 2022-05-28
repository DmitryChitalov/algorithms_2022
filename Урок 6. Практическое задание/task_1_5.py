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

# Задача про компании и их доход

import random

from memory_profiler import profile
from collections import namedtuple
from recordclass import recordclass

QUARTERS_IN_YEAR = 4


@profile
def get_profit(companies_number):
    companies_data = namedtuple(typename='company', field_names='name, profits')

    companies = []
    for _ in range(companies_number):
        name = str(random.randint(1, 1000))
        profits_string = ' '.join([str(random.randint(1, 100)) for i in range(QUARTERS_IN_YEAR)])
        companies.append(companies_data(name=name, profits=list(map(int, profits_string.split()))))

    companies_avg_profits = {}
    for company in companies:
        avg_profit = sum(company.profits) / QUARTERS_IN_YEAR
        companies_avg_profits[company.name] = avg_profit

    total_avg_profit = sum(companies_avg_profits.values()) / len(companies)
    companies_under_avg = [k for k, v in companies_avg_profits.items() if v < total_avg_profit]
    companies_above_avg = [k for k, v in companies_avg_profits.items() if v > total_avg_profit]

    print(f'Средняя годовая прибыль всех предприятий: {total_avg_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {",".join(companies_above_avg)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {",".join(companies_under_avg)}')


@profile
def get_profit_2(companies_number):
    companies_data = recordclass('company', 'name, profits')

    companies = []
    for _ in range(companies_number):
        name = str(random.randint(1, 1000))
        profits_string = ' '.join([str(random.randint(1, 100)) for i in range(QUARTERS_IN_YEAR)])
        companies.append(companies_data(name=name, profits=list(map(int, profits_string.split()))))

    companies_avg_profits = {}
    for company in companies:
        avg_profit = sum(company.profits) / QUARTERS_IN_YEAR
        companies_avg_profits[company.name] = avg_profit

    total_avg_profit = sum(companies_avg_profits.values()) / len(companies)
    companies_under_avg = [k for k, v in companies_avg_profits.items() if v < total_avg_profit]
    companies_above_avg = [k for k, v in companies_avg_profits.items() if v > total_avg_profit]

    print(f'Средняя годовая прибыль всех предприятий: {total_avg_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {",".join(companies_above_avg)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {",".join(companies_under_avg)}')


if __name__ == '__main__':
    get_profit(100000)      # 24.3 MiB
    get_profit_2(100000)    # 20.6 MiB
    # Использование recordclass вместо namedtuple оптимизирует использование памяти
