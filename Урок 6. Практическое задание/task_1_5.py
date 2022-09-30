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
"""
Урок 5 задача 1.
Для замеров упростила задачу и вместо введения с клавиатуры количества предприятий
сделала эту переменную равнцю 1.
Для оптимизации кода использовала recordclass и как показывают измерения объем 
использованной оперативной пямяти сократился. Следовательно использование recordclass
положительно влияет на вычислительные ресурсы.
"""


import sys
from collections import namedtuple
from recordclass import recordclass


def average_profit():
    number = 1
    companies = namedtuple('Company', 'company_name quarter1 quarter2 quarter3 quarter4')
    company_aver_prof = {}
    for i in range(number):
        company = companies(
            company_name=input('Insert name of the company: '),
            quarter1=int(input('Insert profit for the first quarter: ')),
            quarter2=int(input('Insert profit for the second quarter: ')),
            quarter3=int(input('Insert profit for the third quarter: ')),
            quarter4=int(input('Insert profit for the fourth quarter: '))
        )
        company_aver_prof[company.company_name] = (company.quarter1 + company.quarter2 + \
                                                   company.quarter3 + company.quarter4) / 4
        print(f'Объём занимаемой объектом namedtuple памяти: 'f'{sys.getsizeof(company)} байт(а)')

    mutual_aver_profit = 0
    for v in company_aver_prof.values():
        mutual_aver_profit += v
    mutual_aver_profit = mutual_aver_profit / number
    print(f'Average annual profit is: {mutual_aver_profit}')


    for k, v in company_aver_prof.items():
        if v == mutual_aver_profit:
            print(f'{k} is a company with the average profit.')
        elif v < mutual_aver_profit:
            print(f'{k} is a company with the profit below average.')
        elif v > mutual_aver_profit:
            print(f'{k} is a company with the profit above average.')


average_profit()


def average_profit():
    number = 1
    companies = recordclass('Company', 'company_name quarter1 quarter2 quarter3 quarter4')
    company_aver_prof = {}
    for i in range(number):
        company = companies(
            company_name=input('Insert name of the company: '),
            quarter1=int(input('Insert profit for the first quarter: ')),
            quarter2=int(input('Insert profit for the second quarter: ')),
            quarter3=int(input('Insert profit for the third quarter: ')),
            quarter4=int(input('Insert profit for the fourth quarter: '))
        )
        company_aver_prof[company.company_name] = (company.quarter1 + company.quarter2 + \
                                                   company.quarter3 + company.quarter4) / 4
        print(f'Объём занимаемой объектом recordclass памяти: 'f'{sys.getsizeof(company)} байт(а)')

    mutual_aver_profit = 0
    for v in company_aver_prof.values():
        mutual_aver_profit += v
    mutual_aver_profit = mutual_aver_profit / number
    print(f'Average annual profit is: {mutual_aver_profit}')


    for k, v in company_aver_prof.items():
        if v == mutual_aver_profit:
            print(f'{k} is a company with the average profit.')
        elif v < mutual_aver_profit:
            print(f'{k} is a company with the profit below average.')
        elif v > mutual_aver_profit:
            print(f'{k} is a company with the profit above average.')


average_profit()

""" 
#Объём занимаемой объектом namedtuple памяти: 80 байт(а)
#Объём занимаемой объектом recordclass памяти: 56 байт(а)

"""
