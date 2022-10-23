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

dct_enterprise = {}
enterprise = namedtuple('enterprise', ['p1', 'p2', 'p3', 'p4'])
count = int(input("Количество предприятий: "))

for i in range(count):
    enterprise_name = input(str(i + 1) + '-е предприятие: ')
    enterprise_profit = input('через пробел введите прибыль данного предприятия\n'
                              'за каждый квартал(Всего 4 квартала): ').split(' ')
    dct_enterprise[enterprise_name] = enterprise(
        p1=int(enterprise_profit[0]),
        p2=int(enterprise_profit[1]),
        p3=int(enterprise_profit[2]),
        p4=int(enterprise_profit[3])
        )

total_profit = ()

for name, profit in dct_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(dct_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')
for name, profit in dct_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in dct_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')