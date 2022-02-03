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


# Использовать named tuple

from audioop import avg
from collections import namedtuple


Company = namedtuple('Company', ['name', 'income'])


def input_companies():
    companies = []
    companies_count = int(
        input('Введите количество предприятий для расчета прибыли: '))
    for i in range(0, companies_count):
        name = input('Введите название предприятия: ')
        income_str = input('через пробел введите прибыль данного предприятия \n'
                           'за каждый квартал(Всего 4 квартала): ')
        income = [int(value) for value in income_str.split()]
        companies.append(Company(name, income))
    return companies


#companies = [
#    Company('Mss', [1000, 1500, 2000]),
#    Company('Asd', [758, 678, 1000]),
#    Company('Mvd', [500, 650, 1500]),
#    Company('Zmy', [100, 150, 200]),
#    Company('Ntd', [300, 450, 640])
#]

companies = input_companies()

avg_income = sum([sum(company.income)
                 for company in companies]) / len(companies)
print('Средняя годовая прибыль всех предприятий: ', avg_income)

gr_than_avg_list = [company.name for company in companies if
                    sum(company.income) > avg_income]
print('Предприятия, с прибылью выше среднего значения: ', *gr_than_avg_list)

ls_than_avg_list = [company.name for company in companies if
                    sum(company.income) < avg_income]
print('Предприятия, с прибылью ниже среднего значения: ', *ls_than_avg_list)
