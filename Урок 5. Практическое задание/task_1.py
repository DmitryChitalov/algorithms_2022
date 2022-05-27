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
from collections import OrderedDict
# from functools import reduce


def calc_profit_enterprises():
    less_average_profit = []
    more_average_profit = []
    count_sum = 0
    dict_enterprises = OrderedDict()
    num_enterprises = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(num_enterprises):
        name_company = input(f'Введите название {i + 1} предприятия: ')
        profit_company = input('Через пробел введите прибыль данного предприятия '
                               'за каждый квартал(Всего 4 квартала): ')
        profit_year = sum([int(el) for el in profit_company.split(' ')])
        dict_enterprises[name_company] = profit_year
        count_sum += profit_year
    all_average_profit = count_sum / num_enterprises
    for k, v in dict_enterprises.items():
        if float(v) > all_average_profit:
            more_average_profit.append(k)
        elif float(v) <= all_average_profit:
            less_average_profit.append(k)
    return f'Средняя годовая прибыль всех предприятий: {all_average_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(more_average_profit)}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(less_average_profit)}'


print(calc_profit_enterprises())
