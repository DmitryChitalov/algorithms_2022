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

from collections import defaultdict, namedtuple
'''
companies = defaultdict(list)


qnt = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(qnt):
    company_name = input('Введите название предприятия: ')
    company_income = input('через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
    for el in company_income.split(' '):
        companies[company_name].append(int(el))

companies_year_income = {}
for i in companies.keys():
    companies_year_income[i] = sum(companies[i])

median = (sum(companies_year_income.values())) / qnt

good_income = []
bad_income = []
for key in companies_year_income.keys():
    if companies_year_income[key] < median:
        bad_income.append(key)
    elif companies_year_income[key] > median:
        good_income.append(key)

print(f'Средняя годовая прибыль всех предприятий: {median} \n'
      f'Предприятия, с прибылью выше среднего значения: {good_income} \n'
      f'Предприятия, с прибылью ниже среднего значения: {bad_income}')

'''
'''Вариант решения с NamedTuple'''

company = namedtuple('company', ['name', 'quarterly_incomes', 'year_income'])
companies = list()

qnt = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(qnt):
    company_name = input('Введите название предприятия: ')
    company_income = input('через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
    temp_income_list = list()
    for el in company_income.split(' '):
        temp_income_list.append(int(el))
    companies.append(company(company_name, temp_income_list, sum(temp_income_list)))

print(companies)

total_income = 0
for i in companies:
    total_income += i.year_income
median = total_income/qnt

good_income = []
bad_income = []
for i in companies:
    if i.year_income < median:
        bad_income.append(i.name)
    elif i.year_income > median:
        good_income.append(i.name)

print(f'Средняя годовая прибыль всех предприятий: {median} \n'
      f'Предприятия, с прибылью выше среднего значения: {good_income} \n'
      f'Предприятия, с прибылью ниже среднего значения: {bad_income}')
