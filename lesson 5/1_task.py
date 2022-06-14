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


def org_info():
    info = namedtuple('Organisation', 'name profit')
    dct = {}
    org_count = int(input('Enter number of organisations: '))
    result = {'Organisations with profit less than average: ': [],
              'Organisations with profit higher than average: ': []}
    for el in range(org_count):
        organisation = info(name=input('Enter name of organisation: '),
                            profit=sum(list(map(int, input('Enter profit per quarter sep. by space : ').split()))))
        dct[organisation.name] = organisation.profit
    avg_profit = round(sum(dct.values()) / org_count, 2)
    for key, value in dct.items():
        if value < avg_profit:
            result['Organisations with profit less than average: '].append(key)
        else:
            result['Organisations with profit higher than average: '].append(key)
    print(f'Average profit: {avg_profit}')
    for item in result.items():
        print(item)


def org_info_2():
    result = defaultdict(list)
    org_count = int(input('Enter number of organisations: '))
    organisations = {}
    total_profit = 0
    for el in range(org_count):
        name = input('Enter name of organisation: ')
        profit = sum(list(map(int, input('Enter profit per quarter sep. by space : ').split())))
        total_profit += profit
        organisations[name] = profit
    avg_profit = round(total_profit / (org_count * 4), 2)
    for key, value in organisations.items():
        if value < avg_profit:
            result['less'].append(key)
        else:
            result['higher'].append(key)
    print(f'Average profit: {avg_profit}')
    print(f'Organisations with profit less than average: {",".join(f"{el}" for el in result["less"])}')
    print(f'Organisations with profit higher than average: {", ".join(f"{el}" for el in result["higher"])}')


org_info()
# org_info_2()
