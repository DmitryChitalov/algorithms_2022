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
несколько вариантов решения этого задания,
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

try:
    companies_number = int(input('Введите количество предприятий для расчета прибыли: '))
    if companies_number < 0:
        print('Вы ввели отрицательное число.')
        exit()
    Company = namedtuple('Company', 'company_name, annual_profit')
    companies_list = []
    sum_annual_profit = 0
    _companies_number = companies_number
    while _companies_number > 0:
        company_name = input('Введите название предприятия: ')
        quarterly_profit_list = input('Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ').split()
        while len(quarterly_profit_list) != 4:
            quarterly_profit_list = input('Вы ввели прибыль не за 4 квартала. Попробуйте ещё раз: ').split()
        annual_profit = sum([float(el) for el in quarterly_profit_list])
        sum_annual_profit += annual_profit
        company = Company(
            company_name,
            annual_profit
        )
        companies_list.append(company)
        _companies_number -= 1

    avg_annual_profit = sum_annual_profit / companies_number
    companies_above_avg_annual_profit = []
    companies_below_avg_annual_profit = []

    for cmp in companies_list:
        if cmp.annual_profit > avg_annual_profit:
            companies_above_avg_annual_profit.append(cmp.company_name)
        elif cmp.annual_profit < avg_annual_profit:
            companies_below_avg_annual_profit.append(cmp.company_name)

    print(f'Средняя годовая прибыль всех предприятий: {avg_annual_profit}')
    if companies_number > 1:
        print(f"Предприятия с прибылью выше среднего значения: "
              f"{', '.join(companies_above_avg_annual_profit)}")
        print(f"Предприятия с прибылью ниже среднего значения: "
              f"{', '.join(companies_below_avg_annual_profit)}")
except ValueError:
    print('Вы ввели не число.')
except ZeroDivisionError:
    exit()
