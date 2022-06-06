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
Это файл для первого скрипта
"""
from memory_profiler import profile
# from memory_profiler import memory_usage
from collections import namedtuple
from recordclass import recordclass

# Декоратор для замера памяти скрипта
# def mib_size(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_dif = m2[0] - m1[0]
#         return mem_dif, res
#
#     return wrapper


'''Скрипт урока №5 задание №1 (посчитать среднюю прибыль всех предприятий,
и вывести предприятия у которх средняя прибыль ниже общей средней прибыли,
и предприятия с прибылью выше общей средней прибыли)'''


# @mib_size
@profile
def average_profit():
    n = int(input('Введите количество предприятий для расчета прибыли: '))

    def company_tuple(comp, profits):
        res = namedtuple(comp, 'name profit')
        company_profit = res(
            comp,
            profit=profits
        )
        return company_profit

    lst_comoany = []
    i = 0
    sum_profit = 0
    while n != i:
        company = input('Введите имя компании: ')
        profit = input('Введите приболь за 4 квартала через пробел: ')
        lst_comoany.append(company_tuple(company, profit))
        i += 1
        sum_profit += sum(list(map(int, profit.split(' '))))
    less = []
    more = []
    for i in lst_comoany:
        comp_sum = sum(list(map(int, i.profit.split(' '))))
        if sum_profit / n > comp_sum:
            less.append(i.name)
        else:
            more.append(i.name)
    return f'Средняя годовая прибыль всех предприятий: {sum_profit / 2},' \
           f' \nПредприятия, с прибылью выше среднего значения: {more},' \
           f' \nПредприятия, с прибылью ниже среднего значения: {less}'


# @mib_size
@profile
def average_profit_optimize():
    n = int(input('Введите количество предприятий для расчета прибыли: '))

    def company_tuple(comp, profits):
        res = recordclass(comp, 'name profit')
        company_profit = res(
            comp,
            profit=profits
        )
        return company_profit

    lst_comoany = []
    i = 0
    sum_profit = 0
    while n != i:
        company = input('Введите имя компании: ')
        profit = input('Введите приболь за 4 квартала через пробел: ')
        lst_comoany.append(company_tuple(company, profit))
        i += 1
        sum_profit += sum(list(map(int, profit.split(' '))))
    less = []
    more = []
    for i in lst_comoany:
        comp_sum = sum(list(map(int, i.profit.split(' '))))
        if sum_profit / n > comp_sum:
            less.append(i.name)
        else:
            more.append(i.name)
    return f'Средняя годовая прибыль всех предприятий: {sum_profit / 2},' \
           f' \nПредприятия, с прибылью выше среднего значения: {more},' \
           f' \nПредприятия, с прибылью ниже среднего значения: {less}'


if __name__ == '__main__':
    average_profit()
    average_profit_optimize()

'''
Оптимизировал скрипт при помощи модуля recordclass,
заменил nemedtuple на recordclass, и проверил на одинаковых данных.
Замер моим декоратором @mib_size:
не оптимезированый скрипт занимал 0.0703125 Mib памяти,
а оптимизированный -0.05078125 Mib

Замер с помощью @profile в варианте с namedtuple:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    48     20.0 MiB     20.0 MiB           1   @profile
    49                                         def average_profit():
    50     20.1 MiB      0.0 MiB           1       n = int(input('Введите количество предприятий для расчета прибыли: '))
    51                                         
    52     20.1 MiB     -0.0 MiB           3       def company_tuple(comp, profits):
    53     20.1 MiB     -0.0 MiB           2           res = namedtuple(comp, 'name profit')
    54     20.1 MiB     -0.1 MiB           4           company_profit = res(
    55     20.1 MiB     -0.1 MiB           2               comp,
    56     20.1 MiB     -0.1 MiB           2               profit=profits
    57                                                 )
    58                                                 # sum_profit = sum(list(map(int, company_profit.profit.split(' '))))
    59     20.1 MiB     -0.1 MiB           2           return company_profit
    
    
Замер оптимизированного скрипта с использование recordclass:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    83     20.1 MiB     20.1 MiB           1   @profile
    84                                         def average_profit_optimize():
    85     20.1 MiB      0.0 MiB           1       n = int(input('Введите количество предприятий для расчета прибыли: '))
    86                                         
    87     20.1 MiB      0.0 MiB           3       def company_tuple(comp, profits):
    88     20.1 MiB      0.0 MiB           2           res = recordclass(comp, 'name profit')
    89     20.1 MiB      0.0 MiB           4           company_profit = res(
    90     20.1 MiB      0.0 MiB           2               comp,
    91     20.1 MiB      0.0 MiB           2               profit=profits
    92                                                 )
    93                                                 # sum_profit = sum(list(map(int, company_profit.profit.split(' '))))
    94     20.1 MiB      0.0 MiB           2           return company_profit
    
    
Не знаю, что значит '-' в таблице increment в первом варианте.
думаю оптимизация с использованием recordclass работает.
'''
