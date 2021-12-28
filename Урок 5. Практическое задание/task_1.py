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


class Companies:
    DATA = []
    quarts = ('I', 'II', 'III', 'IV')

    def __init__(self, name: str, data):
        self.name = name
        self.data = data
        self.info = namedtuple(name, Companies.quarts)(*data)
        Companies.DATA.append(self.info)

    def mean(self):
        return mean(list(self.data))

    @classmethod
    def all_mean(cls):
        return mean([list(i) for i in cls.DATA])

    def __repr__(self):
        return f'{self.name}'


def analyzing():
    companies = []
    n = int(input('Input amount of companies: '))
    i = 0
    while n > i:
        name = input('Input company name: ').strip()
        values = map(int, input('Input data of company: ').replace(',', ' ').split())
        company = Companies(name, values)
        companies.append(company)
        i += 1
    print(f'Средняя прибыль всех компаний за год: {Companies.all_mean()}')
    for i in companies:
        if i.mean() < Companies.all_mean():
            print(f'Предприятие, с прибылью ниже среднего значения: {i.name}')
        else:
            print(f'Предприятие, с прибылью выше среднего значения: {i.name}')
    return companies


if __name__ == '__main__':
    result = analyzing()
    print(result)