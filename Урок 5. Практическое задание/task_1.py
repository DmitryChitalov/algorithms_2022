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


def company_profit_interface():
    cnt = namedtuple('Company', 'company_name quarter_one quarter_two quarter_three quarter_four')
    company_dict, company_top, company_unprofitable = {}, [], []
    company_count = int(input('Введите количество предприятий для расчета прибыли: '))
    for company in range(company_count):
        _company_name = input('Введите название предприятия: ')
        _company_profit = input(
            'через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ').split()
        company_parts = cnt(
            company_name=_company_name,
            quarter_one=_company_profit[0],
            quarter_two=_company_profit[1],
            quarter_three=_company_profit[2],
            quarter_four=_company_profit[3],
        )
        company_dict[company] = company_parts
    average_revenue = company_average_revenue(company_dict)
    for company in company_dict.values():
        if company_year_profit(company) >= average_revenue:
            company_top.append(company.company_name)
        else:
            company_unprofitable.append(company.company_name)
    print(f'Средняя годовая прибыль всех предприятий: {average_revenue}')
    print('Предприятия, с прибылью выше среднего значения: ', *company_top)
    print('Предприятия, с прибылью ниже среднего значения: ', *company_unprofitable)


def company_average_revenue(company_dict):
    """
    Расчет среднегодовой прибыли всех кампаний
    :param company_dict: Namedtuple
    :return: Integer, средний доход за год
    """
    average_revenue = 0
    for company in company_dict.values():
        average_revenue += int(company.quarter_one)
        average_revenue += int(company.quarter_two)
        average_revenue += int(company.quarter_three)
        average_revenue += int(company.quarter_four)

    return average_revenue / len(company_dict)


def company_year_profit(company):
    """
    Расчет годовой прибыли для одной компании
    :param company: Namedtuple
    :return: Integer
    """
    year_profit = int(company.quarter_one)
    year_profit += int(company.quarter_two)
    year_profit += int(company.quarter_three)
    year_profit += int(company.quarter_four)
    return year_profit


if __name__ == '__main__':
    company_profit_interface()
