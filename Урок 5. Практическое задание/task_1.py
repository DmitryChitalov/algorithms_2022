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

# from collections import defaultdict
#
#
from collections import defaultdict
from statistics import mean
#
dict_company = defaultdict(int)
qty_company = int(input('Please input companies Qty: '))

for i in range(qty_company):
    company_name = input('Please input a company name: ')
    company_profit = input('Please fill in an quarter profit via space in RUB, millions (Sample: 40 50 55 45): ')
    dict_company[company_name] = mean([int(i) for i in company_profit.split()])

average_profit = mean(dict_company.values())
max_profit = [i for i in dict_company.keys() if dict_company[i] > average_profit]
min_profit = [i for i in dict_company.keys() if dict_company[i] < average_profit]

print(f'Total average profit: {average_profit}')
print(f'Companies with profit greater than total average profit: {max_profit}')
print(f'Companies with profit less than total average profit: {min_profit}')




