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
from collections import defaultdict


def profit_calculation(profit, num):
    """
    Функция считает среднюю годовую прибыль по предприятиям,
    определяет пердприятия с большей и меньшей прибылью
    :param profit: dict
    :param num: int
    :return: str
    """
    profit_company = defaultdict(int)
    total_profit = 0
    above_average = ''
    below_average = ''
    for k, v in profit.items():
        for i in v:
            total_profit += float(i)
            profit_company[k] += float(i)
    total_profit = total_profit / num
    max_profit = max(profit_company.values())
    min_profit = min(profit_company.values())
    for k, v in profit_company.items():
        if v == max_profit:
            above_average = k
        elif v == min_profit:
            below_average = k

    return f'Средняя годовая прибыль всех предприятий: {total_profit}\n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {below_average}'


if __name__ == '__main__':
    number_enterprises = int(input('Введите количество предприятий: '))
    data_company = defaultdict(list)
    for _ in range(number_enterprises):
        name_company = input('Введите название компании: ')
        profit_quarter = input('через пробел введите прибыль данного предприятия'
                               'за каждый квартал(Всего 4 квартала): ').split()
        data_company[name_company] = profit_quarter

    print(profit_calculation(data_company, number_enterprises))
