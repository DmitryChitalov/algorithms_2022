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
# Курс Алгоритмы и структуры данных, Урок 5, задание 1
from collections import namedtuple
from statistics import mean
from memory_profiler import profile
from random import choice, randint
from string import ascii_letters
from recordclass import recordclass

companies_quarters_namedtuple = namedtuple('Company', 'company_name quarters')
companies_quarters_recordclass = recordclass('Company', 'company_name quarters')


@profile
def companies_info():
    quarter_list = []
    companies_list = []
    less_than_avg_companies = []
    more_than_avg_companies = []
    try:
        number = 10000
    except ValueError:
        print('You have to enter a number, not a string')
        return
    for i in range(number):
        company_name = ''.join(choice(ascii_letters) for i in range(12))
        quarters = f'{randint(1, 1000000)} {randint(1, 1000000)} {randint(1, 1000000)} {randint(1, 1000000)}'
        i = companies_quarters_namedtuple(company_name, quarters)
        quarter_list.extend(i.quarters.split())
        companies_list.append(i)
    avg_total_quarters = mean(map(int, quarter_list))
    print(f'Average profit of each company: {avg_total_quarters}')
    for v in range(len(companies_list)):
        if sum(map(int, companies_list[v].quarters.split())) < avg_total_quarters:
            less_than_avg_companies.append(companies_list[v].company_name)
        else:
            more_than_avg_companies.append(companies_list[v].company_name)
    print(f'Companies with above-average profits: {more_than_avg_companies}\n'
          f'Companies with below-average profits: {less_than_avg_companies}')


@profile
def companies_info_opt():
    avg_total_quarters = 0
    companies_list = []
    less_than_avg_companies = []
    more_than_avg_companies = []
    try:
        number = 10000
    except ValueError:
        print('You have to enter a number, not a string')
        return
    for i in range(number):
        company_name = ''.join(choice(ascii_letters) for i in range(12))
        quarters = f'{randint(1, 1000000)} {randint(1, 1000000)} {randint(1, 1000000)} {randint(1, 1000000)}'
        i = companies_quarters_recordclass(company_name, quarters.split())
        companies_list.append(i)
        avg_total_quarters += mean(map(int, i.quarters))
    print(f'Average profit of each company: {avg_total_quarters}')
    for v in range(len(companies_list)):
        if sum(map(int, companies_list[v].quarters)) < avg_total_quarters:
            less_than_avg_companies.append(companies_list[v].company_name)
        else:
            more_than_avg_companies.append(companies_list[v].company_name)
    print(f'Companies with above-average profits: {more_than_avg_companies}\n'
          f'Companies with below-average profits: {less_than_avg_companies}')


companies_info()
companies_info_opt()
print('\nВывод: оптимизировал код сменив namedtuple на recordclass')
