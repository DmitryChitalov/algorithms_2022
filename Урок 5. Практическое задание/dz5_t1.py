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
import random


def sum_tuple(numbers):
    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


company = collections.namedtuple('company', ['q1', 'q2', 'q3', 'q4'])

company_base = {}


"""
n = int(input("Количество предприятий: "))
for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_1 = int(input('Прибыль за 1-й квартал: '))
    profit_2 = int(input('Прибыль за 2-й квартал: '))
    profit_3 = int(input('Прибыль за 3-й квартал: '))
    profit_4 = int(input('Прибыль за 4-й квартал: '))
    company_base[name] = company(
        q1=profit_1,
        q2=profit_2,
        q3=profit_3,
        q4=profit_4
    )
"""

company_base['company_1'] = company(
    q1=random.randint(0, 1000000),
    q2=random.randint(0, 1000000),
    q3=random.randint(0, 1000000),
    q4=random.randint(0, 1000000)
)

company_base['company_2'] = company(
    q1=random.randint(0, 1000000),
    q2=random.randint(0, 1000000),
    q3=random.randint(0, 1000000),
    q4=random.randint(0, 1000000)
)

total_profit = ()

for name, profit in company_base.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

midl_profit = sum(total_profit) / len(company_base)
print(f'Средняя прибыль за год для всех предприятий {midl_profit}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in company_base.items():
    if sum(profit) > midl_profit:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')

for name, profit in company_base.items():
    if sum(profit) < midl_profit:
        print(f'{name} - {sum(profit)}')