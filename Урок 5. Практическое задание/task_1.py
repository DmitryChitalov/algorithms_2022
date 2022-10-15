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

companies = namedtuple('Companies', 'id name quarter_1 quarter_2 quarter_3 quarter_4')

def companies_profit():
    id = 0
    average_profit_of_companies = {}
    general_profit = 0
    total_profit = 0

    num_of_companies = int(input('Введите количество предприятий: '))

    for i in range(num_of_companies):
        id += 1
        company = companies(id, name=input('Введите название предприятия: '),
                            quarter_1=int(input('Введите прибыль за первый квартал: ')),
                            quarter_2=int(input('Введите прибыль за второй квартал: ')),
                            quarter_3=int(input('Введите прибыль за третий квартал: ')),
                            quarter_4=int(input('Введите прибыль за четвертый квартал: '))
                            )
        average_profit = (company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4
        average_profit_of_companies[company.name] = average_profit


    for i in average_profit_of_companies.values():
        general_profit += i

    profit_of_companies_lower_than_average = [i for i, j in average_profit_of_companies.items()
                                              if j < general_profit / 4]
    profit_of_companies_higher_than_average = [i for i, j in average_profit_of_companies.items()
                                               if j >= general_profit / 4]

    total_profit += average_profit
    profit = total_profit / num_of_companies

    return f'Средняя годовая прибыль всех предприятий: {profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {profit_of_companies_higher_than_average}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {profit_of_companies_lower_than_average}'


print(companies_profit())
