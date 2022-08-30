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

import re
from collections import namedtuple


def get_firm():
    Firm = namedtuple('Firm', 'firm_name total_profit')
    profit_pattern = r'^([\d]+\s){3}[\d]+$'

    firm_name = input('Введите название предприятия: ')
    while True:
        firm_profit = input('Через пробел введите прибыль данного предприятия '
                            'за каждый квартал (Всего 4 квартала): ')

        if re.fullmatch(profit_pattern, firm_profit):
            profit_list = list(map(int, firm_profit.split()))
            return Firm(firm_name, sum(profit_list))
        else:
            print('Введены неверные данные!')


def get_count():
    while True:
        try:
            return int(input('Введите количество предприятий для расчета прибыли: '))
        except ValueError:
            print('Введено не число!')


def main():
    firms = []
    firms_count = get_count()

    for _ in range(firms_count):
        firms.append(get_firm())

    if len(firms) == 1:
        print(f'{firms[0].firm_name} - единственное предприятие, годовая прибыль: {firms[0].total_profit}')
    else:
        mean_profit = round(sum([firm.total_profit for firm in firms]) / firms_count, 2)
        greater_profit = []
        less_profit = []

        for firm in firms:
            if firm.total_profit > mean_profit:
                greater_profit.append(firm.firm_name)
            elif firm.total_profit < mean_profit:
                less_profit.append(firm.firm_name)

        print(f'Средняя годовая прибыль всех предприятий: {mean_profit}')
        print(f'Предприятия с прибылью выше среднего значения: {", ".join(greater_profit)}')
        print(f'Предприятия с прибылью ниже среднего значения: {", ".join(less_profit)}')


if __name__ == '__main__':
    main()
