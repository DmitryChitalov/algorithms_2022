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
from collections import  namedtuple

COMPANY = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')


def profit():
    quantity = int(input('Введите количество предприятий для расчета прибыли: '))
    all_companies = []
    average_profit = 0
    for i in range(quantity):
        name = input('Введите название предприятия: ')
        profit = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split(' ')
        user_company = COMPANY(
            name=name,
            quarter_1=int(profit[0]),
            quarter_2=int(profit[1]),
            quarter_3=int(profit[2]),
            quarter_4=int(profit[3])
        )
        all_companies.append(user_company)
    for company in all_companies:
        average_profit += sum(company[1:]) / len(all_companies)
    bad_companies = [company.name for company in all_companies if sum(company[1:]) < average_profit]
    good_companies = [company.name for company in all_companies if sum(company[1:]) > average_profit]
    return f'Средняя годовая прибыль всех предприятий: {average_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {good_companies}\n' \
           f'Предприятия с прибылью ниже среднего значения: {bad_companies}'


if __name__ == '__main__':
    print(profit())
