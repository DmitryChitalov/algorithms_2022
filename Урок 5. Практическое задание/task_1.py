"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple


def profit():
    tuple_name = 'Company'
    n = int(input('Введите количество предприятий: '))
    COMP = namedtuple(tuple_name, 'name first second third fourth')
    comp_av_profit = {}

    for i in range(n):
        company = COMP(name=input('Введите название предприятия: '),
                       first=float(input('Введите прибыль за первый квартал: ')),
                       second=float(input('Введите прибыль за второй квартал: ')),
                       third=float(input('Введите прибыль за третий квартал: ')),
                       fourth=float(input('Введите прибыль за четвертый квартал: ')))
        comp_av_profit[company.name] = (company.first + company.second + company.third + company.fourth)

    av_profit = 0
    for value in comp_av_profit.values():
        av_profit += value
    av_profit = av_profit / n

    low_profit = []
    high_profit = []
    av_profit_list = []
    for key, value in comp_av_profit.items():
        if value < av_profit:
            low_profit.append(key)
        elif value > av_profit:
            high_profit.append(key)
        elif value == av_profit:
            av_profit_list.append(key)

    print(f'Средняя годовая прибыль всех предприятий: {av_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: ')
    for el in high_profit:
        print(el)
    print(f'Предприятия, с прибылью ниже среднего значения: ')
    for el in low_profit:
        print(el)
    print(f'Предприятия, с прибылью равной среднему значению: ')
    for el in av_profit_list:
        print(el)


profit()
