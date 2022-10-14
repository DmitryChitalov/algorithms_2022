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

def average_profit():
    number_of_companies = input('Введите количество компаний для расчета прибыли: ')
    arg_dict = defaultdict(int)
    while len(arg_dict) != int(number_of_companies):
        companies_name = input('Введите названия предприятия: ')
        profit_income = input('Введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        year_income = [int(x) for x in profit_income.split(' ')]
        arg_dict[companies_name] = sum(year_income)
    average_year_income = sum(arg_dict.values()) / int(number_of_companies)
    top_comp = [x for x in arg_dict if arg_dict.get(x) >= average_year_income]
    low_comp = [x for x in arg_dict if arg_dict.get(x) < average_year_income]
    return f'Средняя годовая прибыль всех предприятий: {average_year_income}\n' \
           f'Предприятия, с прибылью выше среднего значения: {top_comp}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {low_comp}'

print(average_profit())

# Решение через именнованные кортежи

def namedtuple_average_profit():
    number_of_companies = input('Введите количество компаний для расчета прибыли: ')
    comp = collections.namedtuple('comp', ['name', 'income']) 
    org_dict = {}
    year_income = []
    for i in range(int(number_of_companies)):
        companies_name = input('Введите названия предприятия: ')
        income = input('Введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        org_dict[i + 1] = comp(companies_name, [int(i) for i in income.split(' ')])
    for i in range(int(number_of_companies)):
        year_income += org_dict[i + 1].income  
    top_org = [org_dict[i].name for i in org_dict if sum(org_dict[i].income) >= sum(year_income) / int(number_of_companies)]
    low_org = [org_dict[i].name for i in org_dict if sum(org_dict[i].income) < sum(year_income) / int(number_of_companies)]
    return f'Средняя годовая прибыль всех предприятий: {sum(year_income) / int(number_of_companies)}\n' \
           f'Предприятия, с прибылью выше среднего значения: {top_org}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {low_org}\n'

print(namedtuple_average_profit())

