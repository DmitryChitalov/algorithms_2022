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
import collections
from collections import defaultdict


def income_co():
    companies_numb = input('Введите количество компаний для расчета прибыли: ')
    org_dict = defaultdict(int)
    while len(org_dict) != int(companies_numb):
        org_name = input('Введите названия предприятия: ')
        income = input('через пробел введите прибыль данного предприятия: ')
        year_income = [int(x) for x in income.split(' ')]
        org_dict[org_name] = sum(year_income)
    average_year_income = sum(org_dict.values()) / int(companies_numb)
    top_org = [x for x in org_dict if org_dict.get(x) >= average_year_income]
    low_org = [x for x in org_dict if org_dict.get(x) < average_year_income]
    return f'Средняя годовая прибыль всех предприятий: {average_year_income}\n' \
           f'Предприятия, с прибылью выше среднего значения: {top_org}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {low_org}'


print(income_co())


def income_co_2():
    companies_numb = input('Введите количество компаний для расчета прибыли: ')
    Orgs = collections.namedtuple('Orgs', ['name', 'income'])  # => именованные кортежи
    org_dict = {}
    year_income = []
    for x in range(int(companies_numb)):
        org_name = input('Введите названия предприятия: ')
        income = input('через пробел введите прибыль данного предприятия: ')
        org_dict[x + 1] = Orgs(org_name, [int(x) for x in income.split(' ')])
    for x in range(int(companies_numb)):
        year_income += org_dict[x + 1].income  # => обращаемся по "доходу" именованного кортежа
    top_org = [org_dict[x].name for x in org_dict if sum(org_dict[x].income) >= sum(year_income) / int(companies_numb)]
    low_org = [org_dict[x].name for x in org_dict if sum(org_dict[x].income) < sum(year_income) / int(companies_numb)]
    return f'Средняя годовая прибыль всех предприятий: {sum(year_income) / int(companies_numb)}\n' \
           f'Предприятия, с прибылью выше среднего значения: {top_org}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {low_org}\n'


print(income_co_2())
