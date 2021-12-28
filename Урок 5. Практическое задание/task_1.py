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
# Namedtuple, default-dict
from collections import namedtuple
from numpy import mean


def analyzing():
    data = {}
    n = int(input('Input amount of companies: '))
    companies = namedtuple('Company', 'name I II III IV')
    for i in range(n):
        name = input('Input company\'s name: ')
        values = tuple(map(int, input('Input the values for the four quarters: ').split()))
        company = companies(name=name, I=values[0], II=values[1], III=values[2], IV=values[3])
        data[company.name] = mean(values)

    total_average = 0
    for v in data.values():
        total_average += v
    total_average = total_average / n

    for k, v in data.items():
        if v > total_average:
            print(f'Profit is above average - {k}')
        elif v < total_average:
            print(f'Profit is low average - {k}')
        elif v == total_average:
            print(f'Average profit - {k}')


if __name__ == '__main__':
    analyzing()
