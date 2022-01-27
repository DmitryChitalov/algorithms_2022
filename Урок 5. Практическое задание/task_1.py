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
from collections import namedtuple, defaultdict

companies_stat = {}
companies = []

number_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(number_of_companies):
    company_name = input('Введите название предприятия: ')
    company = namedtuple(company_name, 'first second third fourth')

    income_str = input('через пробел введите прибыль данного предприятия \nза каждый квартал(Всего 4 квартала): ')
    income_lst = [int(x) for x in income_str.split(' ')]

    company_data = company(
        first=income_lst[0],
        second=income_lst[1],
        third=income_lst[2],
        fourth=income_lst[3]
    )

    # companies_stat[company_name] = 0

    companies.append(company_data)

all_income = 0
for company_income in companies:
    income_per_year = 0
    for income in company_income:
        income_per_year += income

    companies_stat[type(company_income).__name__] = income_per_year
    all_income += income_per_year

avg_income = all_income / number_of_companies

losers = []
winners = []
for name, income in companies_stat.items():
    if income <= avg_income:
        losers.append(name)
    else:
        winners.append(name)


print(f'Средняя годовая прибыль всех предприятий: {avg_income}')
print('Предприятия, с прибылью выше среднего значения: ', end='')
for winner in winners:
    print(winner, end='')
print('\nПредприятия, с прибылью ниже среднего значения: ', end='')
for loser in losers:
    print(loser, end='')
# print(all_income / number_of_companies)
# print(companies_stat, losers, winners)
# print(companies)
