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
"""
# Урок 5. Задание 1
from memory_profiler import profile
from recordclass import recordclass
from collections import namedtuple
from decimal import Decimal, InvalidOperation

Profit = namedtuple('Profit', 'name q1 q2 q3 q4 total')
ProfitRec = recordclass('Profit', 'name q1 q2 q3 q4 total')


@profile
def test_fnc():
    result_list = []

    try:
        cnt = int(input('Введите количество предприятий для расчета прибыли:'))
    except ValueError as err:
        raise ValueError('Вы ввели не целое число!')
    else:
        for _ in range(cnt):
            name = input('Введите название предприятия:')
            profit = input(
                'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):') or '1 1 1 1'
            try:
                profit = tuple(map(Decimal, profit.split()))
            except InvalidOperation as err:
                raise ValueError('Прибыль может быть только вещественным или целым числом!')
            if len(profit) != 4:
                raise ValueError(f'Введено значений: {len(profit)}, а необходимо 4!')
            for i in range(100000):
                result_list.append(Profit(name, *profit, sum(profit)))

        total_avg = sum((x.total for x in result_list)) / len(result_list)
        orgs_more = (x.name for x in result_list if x.total > total_avg)
        orgs_less = (x.name for x in result_list if x.total < total_avg)

        print(f'Средняя годовая прибыль всех предприятий: {total_avg:.2f}')
        print('Предприятия, с прибылью выше среднего значения:', ', '.join(orgs_more))
        print('Предприятия, с прибылью ниже среднего значения:', ', '.join(orgs_less))


@profile
def test_fnc_mem():
    result_list = []

    try:
        cnt = int(input('Введите количество предприятий для расчета прибыли:'))
    except ValueError as err:
        raise ValueError('Вы ввели не целое число!')
    else:
        for _ in range(cnt):
            name = input('Введите название предприятия:')
            profit = input(
                'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):') or '1 1 1 1'
            try:
                profit = tuple(map(Decimal, profit.split()))
            except InvalidOperation as err:
                raise ValueError('Прибыль может быть только вещественным или целым числом!')
            if len(profit) != 4:
                raise ValueError(f'Введено значений: {len(profit)}, а необходимо 4!')
            for i in range(100000):
                result_list.append(ProfitRec(name, *profit, sum(profit)))

        total_avg = sum((x.total for x in result_list)) / len(result_list)
        orgs_more = (x.name for x in result_list if x.total > total_avg)
        orgs_less = (x.name for x in result_list if x.total < total_avg)

        print(f'Средняя годовая прибыль всех предприятий: {total_avg:.2f}')
        print('Предприятия, с прибылью выше среднего значения:', ', '.join(orgs_more))
        print('Предприятия, с прибылью ниже среднего значения:', ', '.join(orgs_less))


if __name__ == '__main__':
    test_fnc()
    test_fnc_mem()

"""
namedtuple заменен на recordclass. 

Цикл 
for i in range(100000):

добавил, чтобы убедиться, что recordclass занимает меньше памяти, чем nemedtuple

Line #    Mem usage    Increment   Line Contents
================================================
    45     17.3 MiB      0.0 MiB   @profile
    46                             def test_fnc():
    47     17.3 MiB      0.0 MiB       result_list = []
    48                             
    49     17.3 MiB      0.0 MiB       try:
    50     17.3 MiB      0.0 MiB           cnt = int(input('Введите количество предприятий для расчета прибыли:'))
    51                                 except ValueError as err:
    52                                     raise ValueError('Вы ввели не целое число!')
    53                                 else:
    54     38.9 MiB     21.6 MiB           for _ in range(cnt):
    55     17.3 MiB    -21.6 MiB               name = input('Введите название предприятия:')
    56     17.3 MiB      0.0 MiB               profit = input(
    57     17.3 MiB      0.0 MiB                   'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):') or '1 1 1 1'
    58     17.3 MiB      0.0 MiB               try:
    59     17.3 MiB      0.0 MiB                   profit = tuple(map(Decimal, profit.split()))
    60                                         except InvalidOperation as err:
    61                                             raise ValueError('Прибыль может быть только вещественным или целым числом!')
    62     17.3 MiB      0.0 MiB               if len(profit) != 4:
    63                                             raise ValueError(f'Введено значений: {len(profit)}, а необходимо 4!')
    64     38.9 MiB     21.5 MiB               for i in range(100000):
    65     38.9 MiB      0.0 MiB                   result_list.append(Profit(name, *profit, sum(profit)))
    66                             
    67     38.9 MiB      0.0 MiB           total_avg = sum((x.total for x in result_list)) / len(result_list)
    68     38.9 MiB      0.0 MiB           orgs_more = (x.name for x in result_list if x.total > total_avg)
    69     38.9 MiB      0.0 MiB           orgs_less = (x.name for x in result_list if x.total < total_avg)
    70                             
    71     38.9 MiB     -0.0 MiB           print(f'Средняя годовая прибыль всех предприятий: {total_avg:.2f}')
    72     38.9 MiB      0.0 MiB           print('Предприятия, с прибылью выше среднего значения:', ', '.join(orgs_more))
    73     38.9 MiB      0.0 MiB           print('Предприятия, с прибылью ниже среднего значения:', ', '.join(orgs_less))
    
    
Line #    Mem usage    Increment   Line Contents
================================================
    76     19.1 MiB      0.0 MiB   @profile
    77                             def test_fnc_mem():
    78     19.1 MiB      0.0 MiB       result_list = []
    79                             
    80     19.1 MiB      0.0 MiB       try:
    81     19.1 MiB      0.0 MiB           cnt = int(input('Введите количество предприятий для расчета прибыли:'))
    82                                 except ValueError as err:
    83                                     raise ValueError('Вы ввели не целое число!')
    84                                 else:
    85     36.5 MiB     17.3 MiB           for _ in range(cnt):
    86     19.1 MiB    -17.3 MiB               name = input('Введите название предприятия:')
    87     19.1 MiB      0.0 MiB               profit = input(
    88     19.1 MiB      0.0 MiB                   'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):') or '1 1 1 1'
    89     19.1 MiB      0.0 MiB               try:
    90     19.1 MiB      0.0 MiB                   profit = tuple(map(Decimal, profit.split()))
    91                                         except InvalidOperation as err:
    92                                             raise ValueError('Прибыль может быть только вещественным или целым числом!')
    93     19.1 MiB      0.0 MiB               if len(profit) != 4:
    94                                             raise ValueError(f'Введено значений: {len(profit)}, а необходимо 4!')
    95     36.5 MiB     17.3 MiB               for i in range(100000):
    96     36.5 MiB      0.0 MiB                   result_list.append(ProfitRec(name, *profit, sum(profit)))
    97                             
    98     36.5 MiB      0.0 MiB           total_avg = sum((x.total for x in result_list)) / len(result_list)
    99     36.5 MiB      0.0 MiB           orgs_more = (x.name for x in result_list if x.total > total_avg)
   100     36.5 MiB      0.0 MiB           orgs_less = (x.name for x in result_list if x.total < total_avg)
   101                             
   102     36.5 MiB      0.0 MiB           print(f'Средняя годовая прибыль всех предприятий: {total_avg:.2f}')
   103     36.5 MiB      0.0 MiB           print('Предприятия, с прибылью выше среднего значения:', ', '.join(orgs_more))
   104     36.5 MiB      0.0 MiB           print('Предприятия, с прибылью ниже среднего значения:', ', '.join(orgs_less))    
"""
