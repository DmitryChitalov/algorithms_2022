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

Это файл для четвертого скрипта
"""

# Урок 5. Курс Алгоритмы.
# Задание 1.
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего

import sys
from collections import defaultdict
from collections import namedtuple
from memory_profiler import profile
from pympler import asizeof
from recordclass import recordclass
from statistics import mean

MY_DEF_DIC = defaultdict(int)
MY_LST = []
COUNT_FIRM = 0


# __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
@profile
def inside_input_firms(inp_num_firm):
    def input_firms(num_firm):
        if num_firm == 0:
            return MY_DEF_DIC

        inp_firm = input('Введите название предприятия: ')
        ls_profit = input('через пробел введите прибыль данного предприятия \n'
                          'за каждый квартал(Всего 4 квартала): ').split()
        profit = 0
        for _ in ls_profit:
            profit = profit + int(_)
        FIRM = namedtuple(inp_firm, 'id firm_name firm_profit')
        print(f'Объём занимаемой объектом namedtuple памяти: {sys.getsizeof(FIRM)} байт(а).')
        print(asizeof.asizeof(FIRM))
        company_data = FIRM(
            id=num_firm,
            firm_name=inp_firm,
            firm_profit=profit,
        )
        MY_DEF_DIC[num_firm] = company_data
        num_firm -= 1
        input_firms(num_firm)

    return input_firms(inp_num_firm)


# __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
@profile
def inside_input_firms_rec(inp_num_firm):
    def input_firms_rec(num_firm):
        if num_firm == 0:
            return MY_DEF_DIC

        inp_firm = input('Введите название предприятия: ')
        ls_profit = input('через пробел введите прибыль данного предприятия \n'
                          'за каждый квартал(Всего 4 квартала): ').split()
        profit = 0
        for _ in ls_profit:
            profit = profit + int(_)
        firm_rec = recordclass(inp_firm, 'id firm_name firm_profit')
        #  При использовании модуля recordclass,
        #  переменные занимают примерно одинаковое количество памяти (сравнимое) с namedtuple,
        #  При измерении получилось, что переменные типа recordclass занимают места чуть-чуть больше,
        #  чем переменные типа namedtuple.
        #  То есть, изменяемость типа практически не увеличивает потребление памяти в данном случае.

        print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(firm_rec)} байт(а).')
        print(asizeof.asizeof(firm_rec))
        company_data = firm_rec(
            id=num_firm,
            firm_name=inp_firm,
            firm_profit=profit
        )
        ls_profit = input('Вы правильно ввели прибыль? Повторите ввод: ').split()
        profit = 0
        for _ in ls_profit:
            profit = profit + int(_)
        firm_rec.firm_profit = profit
        print(f'Изменили объект recordclass прибыль: {profit}')
        print(f'Объём занимаемой объектом recordclass памяти после замены: {sys.getsizeof(firm_rec)} байт(а).')
        MY_DEF_DIC[num_firm] = company_data
        num_firm -= 1
        input_firms_rec(num_firm)

    return input_firms_rec(inp_num_firm)


def average_profit():
    for key, val in MY_DEF_DIC.items():
        MY_LST.append(val.firm_profit)
    ava_prof = mean(MY_LST)
    return ava_prof


def comparison_with_average(ava_prof):
    print('Средняя годовая прибыль всех предприятий:', ava_prof)
    above_average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit > ava_prof])

    print('Предприятия, с прибылью выше среднего значения:', above_average)
    below_average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit < ava_prof])
    print('Предприятия, с прибылью ниже среднего значения:', below_average)
    average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit == ava_prof])
    if average:
        print('Предприятия, с прибылью равной среднему значеню:', average)


if __name__ == '__main__':
    # __________________    И С Х О Д Н О Е     Р Е Ш Е Н И Е     __________________#
    num_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    inside_input_firms(num_firms)

    average_profit()
    comparison_with_average(average_profit())

    # __________________    О П Т И М И З И Р О В А Н Н О Е    Р Е Ш Е Н И Е     __________________#
    MY_DEF_DIC = defaultdict(int)
    MY_LST = []
    COUNT_FIRM = 0

    num_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    inside_input_firms_rec(num_firms)
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет.
    # Increment везде 0. Значение Mem usage не меняетя.

    average_profit()
    comparison_with_average(average_profit())
    # Использование декоратора @profiler из профилировщика memory_profiler
    # проблем с использованием памяти при работе скрипта не выявляет (мал объем данных).
    # Increment везде 0. Значение Mem usage не меняетя.
