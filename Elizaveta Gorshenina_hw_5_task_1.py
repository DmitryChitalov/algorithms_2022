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


def estimate_profit(enterprises_data_list=[]):
    enterprises = namedtuple('enterprises', 'name qtr_profit_1 qtr_profit_2 qtr_profit_3 qtr_profit_4 annual_profit')
    enterprises_num = int(input('Введите количество предприятий: '))
    for num in range(enterprises_num):
        ent_name = input('Введите название предприятия: ')
        prft1, prft2, prft3, prft4 = (float(qtr_profit) for qtr_profit in input(
            'Через пробел введите прибыль данного предприятия за каждый квартал: ').split())
        enterprises_data_list.append(
            enterprises(ent_name, prft1, prft2, prft3, prft4, sum([prft1, prft2, prft3, prft4])))
    average_annual_profit = sum([ent.annual_profit for ent in enterprises_data_list]) / len(enterprises_data_list)
    print('Средняя годовая прибыль всех предприятий: ', average_annual_profit)
    high_profit_ents = [ent.name for ent in enterprises_data_list if ent.annual_profit > average_annual_profit]
    low_profit_ents = [ent.name for ent in enterprises_data_list if ent.annual_profit < average_annual_profit]
    print('Предприятия, с прибылью выше среднего значения: ')
    print(*high_profit_ents, sep=', ')
    print('Предприятия, с прибылью ниже среднего значения: ')
    print(*low_profit_ents, sep=', ')


estimate_profit()
