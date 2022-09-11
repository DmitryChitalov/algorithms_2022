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

Это файл для третьего скрипта
"""

from collections import namedtuple
from memory_profiler import profile


@profile
def average_profit():
    n = int(input('Введите количество предприятий: '))
    main_dct = {}
    companies = namedtuple('companies', 'name profit_1 profit_2 profit_3 profit_4')
    for i in range(n):
        print('Введите построчно имя компании и прибыль за 4 квартала: ')
        company = companies(
            name=input(),
            profit_1=int(input()),
            profit_2=int(input()),
            profit_3=int(input()),
            profit_4=int(input()))
        main_dct[company.name] = (company.profit_1 + company.profit_2 + company.profit_3 + company.profit_4) / 4
    profit_sum = 0
    for value in main_dct.values():
        profit_sum += value
    aver_profit = profit_sum / n
    print('Общая средняя прибыль: ', aver_profit)
    list1 = []
    list2 = []
    for name in main_dct.keys():
        if main_dct[name] > aver_profit:
            list1.append(name)
        else:
            list2.append(name)
    print('Компании с прибылью больше средней: ', list1)
    print('Компании с прибылью меньше  средней: ', list2)


# оптимизируем код, удаляя вручную ссылки, используя del, сразу же как переменная перестает быть нужной
# пометил такие строки коментарием

@profile
def average_profit_1():
    n = int(input('Введите количество предприятий: '))
    main_dct = {}
    companies = namedtuple('companies', 'name profit_1 profit_2 profit_3 profit_4')
    for i in range(n):
        print('Введите построчно имя компании и прибыль за 4 квартала: ')
        company = companies(
            name=input(),
            profit_1=int(input()),
            profit_2=int(input()),
            profit_3=int(input()),
            profit_4=int(input()))
        main_dct[company.name] = (company.profit_1 + company.profit_2 + company.profit_3 + company.profit_4) / 4
    del companies  # оптимизация
    profit_sum = 0
    for value in main_dct.values():
        profit_sum += value
    aver_profit = profit_sum / n
    del profit_sum  # оптимизация
    del n  # оптимизация
    print('Общая средняя прибыль: ', aver_profit)
    list1 = []
    list2 = []
    for name in main_dct.keys():
        if main_dct[name] > aver_profit:
            list1.append(name)
        else:
            list2.append(name)
    print('Компании с прибылью больше средней: ', list1)
    print('Компании с прибылью меньше  средней: ', list2)


average_profit()
average_profit_1()
