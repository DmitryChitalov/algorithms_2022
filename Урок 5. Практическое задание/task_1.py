"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

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


def average_profit():
    my_company = 'Company'
    quantity = int(
        input('Введите количество предприятий для расчета прибыли: '))
    companies = namedtuple(
        my_company, 'title quarter_1 quarter_2 quarter_3 quarter_4')
    companies_profit = {}

    for i in range(quantity):
        title = input('Введите название предприятия: ')

        profit = input(
            'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')

        profit_by_quarters = profit.split()

        if len(profit_by_quarters) == 4:
            company = companies(title,
                                quarter_1=int(profit_by_quarters[0]),
                                quarter_2=int(profit_by_quarters[1]),
                                quarter_3=int(profit_by_quarters[2]),
                                quarter_4=int(profit_by_quarters[3]))
        else:
            print('Ошибка')

        companies_profit[company.title] = (
            company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4

    total_aver = 0
    for value in companies_profit.values():
        total_aver += value
    total_aver = total_aver / quantity

    print(f'Средняя годовая прибыль всех предприятий: {total_aver}')

    for key, value in companies_profit.items():
        if value > total_aver:
            print(f'Предприятие "{key}" - прибыль выше среднего')
        elif value < total_aver:
            print(f'Предприятие "{key}" - прибыль ниже среднего')
        elif value == total_aver:
            print(f'Предприятие "{key}" - средняя прибыль')


average_profit()
