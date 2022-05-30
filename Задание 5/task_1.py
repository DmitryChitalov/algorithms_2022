"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
"""

import collections
from statistics import mean


firms_counter = collections.Counter()
firms_dict = collections.defaultdict(float)

firm_count = int(input('Количество предприятий:'))
for firm_i in range(firm_count):
    name = input(f'Название предприятия {firm_i + 1}:')
    profit_s = input('Прибыль предприятия за каждый квартал (через пробел):')
    firms_counter[name] = sum([float(profit) for profit in profit_s.split()])
    for profit in profit_s.split():
        firms_dict[name] += float(profit)
        
mean_counter = mean(firms_counter.values())
mean_dict = mean(firms_dict.values())

# print(firms_counter)
# print(firms_dict)

print('Counter:')
print(f'Средняя годовая прибыль: {mean_counter}')
print(
    'Предприятия, с прибылью выше среднего значения:',
    f'{", ".join([firm_name for firm_name in firms_counter.keys() if firms_counter[firm_name] > mean_counter])}'
)
print('Предприятия, с прибылью ниже среднего значения:',
    f'{", ".join([firm_name for firm_name in firms_counter.keys() if firms_counter[firm_name] < mean_counter])}'
)

print('Defaultdict:')
print(f'Средняя годовая прибыль: {mean_dict}')
print(
    'Предприятия, с прибылью выше среднего значения:',
    f'{", ".join([firm_name for firm_name in firms_dict.keys() if firms_dict[firm_name] > mean_dict])}'
)
print('Предприятия, с прибылью ниже среднего значения:',
    f'{", ".join([firm_name for firm_name in firms_dict.keys() if firms_dict[firm_name] < mean_dict])}'
)

