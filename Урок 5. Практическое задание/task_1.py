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

QUARTERS_IN_YEAR = 4


def get_profit():
    companies_data = namedtuple(typename='company', field_names='name, profits')

    companies = []
    companies_number = int(input('Введите количество предприятий для расчета прибыли: '))
    for _ in range(companies_number):
        name = input('Введите название предприятия: ')
        profits_string = input("""через пробел введите прибыль данного предприятия
за каждый квартал (всего 4 квартала): """)
        companies.append(companies_data(name=name, profits=list(map(int, profits_string.split()))))

    companies_avg_profits = {}
    for company in companies:
        avg_profit = sum(company.profits) / QUARTERS_IN_YEAR
        companies_avg_profits[company.name] = avg_profit

    total_avg_profit = sum(companies_avg_profits.values()) / len(companies)
    companies_under_avg = [k for k, v in companies_avg_profits.items() if v < total_avg_profit]
    companies_above_avg = [k for k, v in companies_avg_profits.items() if v > total_avg_profit]

    print(f'Средняя годовая прибыль всех предприятий: {total_avg_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {",".join(companies_above_avg)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {",".join(companies_under_avg)}')


if __name__ == '__main__':
    get_profit()
