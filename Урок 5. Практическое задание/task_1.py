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
import collections
import functools


def income1():
    Company = collections.namedtuple('Company', 'name income')
    lst = []
    for i in range(int(input('Enter number of companies:'))):
        name = input('Company name:')
        total_income = sum([int(i) for i in input('Company income separated by space:').split()])
        lst.append(Company(name=name, income=total_income))
    average_income = functools.reduce(lambda x, y: x + y.income, lst, 0) / len(lst)
    print(f"Average income: {average_income:.1f}")
    above = [i.name for i in filter(lambda x: x.income > average_income, lst)]
    print('Above average: ', *above)
    less = [i.name for i in filter(lambda x: x.income < average_income, lst)]
    print('Less then average:', *less)


def income2():
    dct = collections.defaultdict()
    for i in range(int(input('Enter number of companies:'))):
        name = input('Company name:')
        dct[name] = tuple([int(i) for i in input('Company income separated by space:').split()])
    print(dct)
    average_income = functools.reduce(lambda x, y: x + sum(dct[y]), dct, 0) / len(dct)
    print(f"Average income: {average_income:.1f}")
    above = [i for i in dct if sum(dct[i]) > average_income]
    print('Above average: ', *above)
    less = [i for i in dct if sum(dct[i]) < average_income]
    print('Less then average:', *less)


income1()
income2()
