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

Это файл для пятого скрипта
"""
from collections import namedtuple
from recordclass import recordclass
from memory_profiler import profile


@profile
def profits_1():
    companies = []
    total_profit = 0
    company = namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'year'])
    num = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(num):
        name = input('Введите название предприятия: ')
        income = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала)').split(' ')
        year = int(income[0]) + int(income[1]) + int(income[2]) + int(income[3])
        total_profit += year
        companies.append(company(name=name, q1=income[0], q2=income[1], q3=income[2], q4=income[3], year=year))

    avg_profit = total_profit/num
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

    above_avg = []
    below_avg = []
    for company in companies:
        if company.year > avg_profit:
            above_avg.append(company.name)
        else:
            below_avg.append(company.name)
    print('Предприятия, с прибылью выше среднего значения: ', ','.join(above_avg))
    print('Предприятия, с прибылью ниже среднего значения: ', ','.join(below_avg))


@profile
def profits_2():
    companies = []
    total_profit = 0
    company = recordclass('company', ('name', 'q1', 'q2', 'q3', 'q4', 'year'))
    num = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(num):
        name = input('Введите название предприятия: ')
        income = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала)').split(' ')
        year = int(income[0]) + int(income[1]) + int(income[2]) + int(income[3])
        total_profit += year
        companies.append(company(name=name, q1=income[0], q2=income[1], q3=income[2], q4=income[3], year=year))

    avg_profit = total_profit/num
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

    above_avg = []
    below_avg = []
    for company in companies:
        if company.year > avg_profit:
            above_avg.append(company.name)
        else:
            below_avg.append(company.name)
    print('Предприятия, с прибылью выше среднего значения: ', ','.join(above_avg))
    print('Предприятия, с прибылью ниже среднего значения: ', ','.join(below_avg))


profits_1()
profits_2()

# Во втором случае заменил NamedTuple на recordclass