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

from collections import namedtuple, defaultdict


def create():
    i = int(input('Введите количество предприятий: '))
    companies = namedtuple('company', 'name quarter1 quarter2 quarter3 quarter4')
    average_income = {}
    for j in range(i):
        name = input('Введите название предприятия: ')
        income = input('через пробел введите прибыль данного предприятия: ').split()
        a, b, c, d = map(int, income)
        company = companies(
            name=name,
            quarter1=a,
            quarter2=b,
            quarter3=c,
            quarter4=d)
        average_income[company.name] = \
            (company.quarter1 + company.quarter2 + company.quarter3 + company.quarter4) / 4
    print(average_income)
    annual_income = sum(average_income.values()) / i
    print(f'Средняя годовая прибыль всех предприятий: {annual_income}')
    print(
        f'Предприятия, с прибылью выше среднего значения: {[name for name, val in average_income.items() if val > annual_income]}')
    print(
        f'Предприятия, с прибылью ниже среднего значения: {[name for name, val in average_income.items() if val < annual_income]}')


create()


def create_2():
    i = int(input('Введите количество предприятий: '))
    average_income = defaultdict(int)
    for j in range(i):
        name = input('Введите название предприятия: ')
        income = input('через пробел введите прибыль данного предприятия: ').split()
        s = 0
        for val in income:
            s += int(val)
        average_income[name] = s / 4

    print(average_income)
    annual_income = sum(average_income.values()) / i
    print(f'Средняя годовая прибыль всех предприятий: {annual_income}')
    print(
        f'Предприятия, с прибылью выше среднего значения: {[name for name, val in average_income.items() if val > annual_income]}')
    print(
        f'Предприятия, с прибылью ниже среднего значения: {[name for name, val in average_income.items() if val < annual_income]}')


create_2()