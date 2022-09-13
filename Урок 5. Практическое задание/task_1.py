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
from collections import Counter, namedtuple

company_count = Counter()
CompanyTuple = namedtuple('Companies', 'name profit')
tuple_comp = []
count = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(count):
    name_company = input('Введите название предприятия: ')
    profit = input('через пробел введите прибыль данного предприятия'
                   'за каждый квартал(Всего 4 квартала): ')
    profit_company = map(int, list(profit.split(sep=' ')))
    a = sum(profit_company)
    company_count[name_company] = a
    tuple_comp.append(CompanyTuple(name=name_company, profit=a))
    print()
print(company_count)
print(tuple_comp)
average_1 = company_count.total() / count
average_2 = sum(company.profit for company in tuple_comp) / count
print(f'Средняя годовая прибыль всех предприятий в Count: {average_1}')
print(f'Средняя годовая прибыль всех предприятий в namedtuple: {average_2}')
print(f'Предприятия, с прибылью выше среднего значения Count: '
      f'{[key for key, val in company_count.items() if val > average_1]}')
print(f'Предприятия, с прибылью выше среднего значения namedtuple: '
      f'{[company.name for company in tuple_comp if company.profit > average_2]}')
print(f'Предприятия, с прибылью ниже среднего значения Count: '
      f'{[key for key, val in company_count.items() if val < average_1]}')
print(f'Предприятия, с прибылью ниже среднего значения namedtuple: '
      f'{[company.name for company in tuple_comp if company.profit < average_2]}')
