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
from statistics import mean

companies = namedtuple('Company', 'company_name quarters')


def companies_info():
    quarter_list = []
    companies_list = []
    less_than_avg_companies = []
    more_than_avg_companies = []
    try:
        number = int(input('Enter the number of companies for profit calculation: '))
    except ValueError:
        print('You have to enter a number, not a string')
        return
    for i in range(number):
        company_name = input('Enter the name of the company: ')
        quarters = input('Write the profit of each quarter (separated by a space): ')
        i = companies(company_name, quarters)
        quarter_list.extend(i.quarters.split())
        companies_list.append(i)
    avg_total_quarters = mean(map(int, quarter_list))
    print(f'Average profit of each company: {avg_total_quarters}')
    for v in range(len(companies_list)):
        if sum(map(int, companies_list[v].quarters.split())) < avg_total_quarters:
            less_than_avg_companies.append(companies_list[v].company_name)
        else:
            more_than_avg_companies.append(companies_list[v].company_name)
    print(f'Companies with above-average profits: {more_than_avg_companies}\n'
          f'Companies with below-average profits: {less_than_avg_companies}')


companies_info()
