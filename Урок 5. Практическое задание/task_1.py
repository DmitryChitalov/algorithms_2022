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


def app():
    db = []
    sample = namedtuple('Company', "name quarter_1 quarter_2 quarter_3 quarter_4")

    for _ in range(int(input('Введите количество предприятий: '))):
        name = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
        quarter_1, quarter_2, quarter_3, quarter_4 = profit.split(' ')
        company = sample(
            name=name,
            quarter_1=int(quarter_1),
            quarter_2=int(quarter_2),
            quarter_3=int(quarter_3),
            quarter_4=int(quarter_4)
        )
        db.append(company)

    total_average_profit = sum(map(lambda x: x.quarter_1 + x.quarter_2 + x.quarter_3 + x.quarter_4, db)) / len(db)
    print(f'Средняя годовая прибыль всех предприятий: {total_average_profit}')

    companies_above_average = []
    companies_below_average = []
    for company in db:
        company_profit = company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4
        if company_profit > total_average_profit:
            companies_above_average.append(company.name)
        elif company_profit < total_average_profit:
            companies_below_average.append(company.name)
    print(f'Предприятия, с прибылью выше среднего значения: {companies_above_average}')
    print(f'Предприятия, с прибылью ниже среднего значения: {companies_below_average}')


app()
