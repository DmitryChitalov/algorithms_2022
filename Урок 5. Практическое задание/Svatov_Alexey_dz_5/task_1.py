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
import itertools
from collections import namedtuple


def main_info():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    company_list = []
    Company_tuple = namedtuple('Company_tuple', ['name', 'first', 'second', 'third', 'fourth', 'annual_profit'])
    for i in range(count):
        company = input('Введите название предприятия: ')
        cash = list(map(int, input('Через пробел введите прибыль данного предприятия за каждый квартал '
                                   '(Всего 4 квартала): ').split()))
        _ = Company_tuple(company, *cash, round(sum(cash)))
        company_list.append(_)
    return company_list


def analize_info(input_info):
    mean_annual_profit = sum(_.annual_profit for _ in input_info) / len(input_info)
    company_upper_mean = str([_.name for _ in input_info if _.annual_profit >= mean_annual_profit]).strip('[]')
    company_lower_mean = str([_.name for _ in input_info if _.annual_profit < mean_annual_profit]).strip('[]')
    return f'Средняя годовая прибыль всех предприятий: {mean_annual_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {company_upper_mean}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {company_lower_mean}'


print(analize_info(main_info()))
