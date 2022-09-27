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

def average_profit():

    number = int(input('Insert number of companies for analysis: '))
    companies = namedtuple('company', 'company_name quarter1 quarter2 quarter3 quarter4')
    company_aver_prof = {}
    for i in range(number):
        company = companies(
            company_name=input('Insert name of the company: '),
            quarter1=int(input('Insert profit for the first quarter: ')),
            quarter2=int(input('Insert profit for the second quarter: ')),
            quarter3=int(input('Insert profit for the third quarter: ')),
            quarter4=int(input('Insert profit for the fourth quarter: '))
        )
    company_aver_prof[company.company_name] = (company.quarter1 + company.quarter2 + \
            company.quarter3 + company.quarter4) / 4

    mutual_aver_profit = 0
    for v in company_aver_prof.values():
        mutual_aver_profit += v
    mutual_aver_profit = mutual_aver_profit / number

    for k, v in company_aver_prof.items():
        if v == mutual_aver_profit:
            print(f'{k} is a company with the average profit.')
        elif v < mutual_aver_profit:
            print(f'{k} is a company with the profit below average.')
        elif v > mutual_aver_profit:
            print(f'{k} is a company with the profit above average.')




average_profit()