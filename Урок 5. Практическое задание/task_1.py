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

def profit():
    companies = []  # для сохранения компаний
    above = []      # прибыль выше среднего
    below = []      # прибыль ниже среднего
    Company = namedtuple('Company', 'first second third fourth profit title')
    total_profit = 0
    n = int(input('Введите колличество предприятий: '))

    for i in range(n):
        name = input('Введите название предприятия: ')
        s = input('Введите через пробел прибыль предприятия за каждый квартал: ')
        a = [int(x) for x in s.split()]
        new_company = Company(first=a[0], second=a[1], third=a[2], fourth=a[3],
                       profit=(int(a[0])+int(a[1])+int(a[2])+int(a[3])), title=name)
        companies.append(new_company)

    for company in companies:
        total_profit += company.profit

    mean_profit = total_profit / len(companies)
    print(f'Средняя годовая прибыль всех предприятий: {mean_profit}')

    for company in companies:
        if company.profit > mean_profit:
            above.append(company.title)
        else:
            below.append(company.title)
    print(f'редприятия, с прибылью выше среднего значения: {above}')
    print(f'Предприятия, с прибылью ниже среднего значения: {below}')

    return companies

profit()