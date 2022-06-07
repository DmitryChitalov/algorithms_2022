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
from statistics import mean

company = collections.namedtuple('company', ['name', 'average_profit'])
companys = []
total_average_profit = 0
quant_firm = int(input('Введите количество предприятий для расчета прибыли:\n'))
for i in range(quant_firm):
    name_firm = input('Введите название предприятия:\n')
    profit_quarter = input(
        f'Через пробел введите прибыль предприятия {name_firm} за каждый квартал(Всего 4 квартала):\n')
    avg = mean([int(el) for el in profit_quarter.split(" ")])
    total_average_profit += avg
    companys.append(company(name=name_firm, average_profit=avg))

total_average_profit = total_average_profit / quant_firm
print(f"Компании с прибылью выше средней {total_average_profit}: ")
for company in companys:
    if company.average_profit >= total_average_profit:
        print(company.name)
print(f"Компании с прибылью ниже средней {total_average_profit}: ")
for company in companys:
    if company.average_profit < total_average_profit:
        print(company.name)
