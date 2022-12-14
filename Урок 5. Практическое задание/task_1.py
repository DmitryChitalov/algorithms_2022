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

COMP = namedtuple('Company', 'name yearly_profit')
companies = []

number_of_comps = int(input('Введите число компаний: '))
while number_of_comps > 0:
    comp_name = input('Введите название компании: ')
    quarters = input('Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
    quarters = [int(q) for q in quarters.split(' ')]
    curr_comp = COMP(
        name=comp_name,
        yearly_profit=sum(quarters)
        )
    companies.append(curr_comp)
    number_of_comps -= 1

def get_mean(array):
    return sum(array) / len(array)

average_yearly_profit = get_mean([comp.yearly_profit for comp in companies])

companies_with_low_profit = []
companies_with_high_profit = []

for comp in companies:
    if comp.yearly_profit < average_yearly_profit:
        companies_with_low_profit.append(comp.name)
    elif comp.yearly_profit > average_yearly_profit:
        companies_with_high_profit.append(comp.name)

print('Средняя годовая прибыль всех предприятий: ' + str(average_yearly_profit))
print('Предприятия, с прибылью выше среднего значения: ' + ', '.join(companies_with_high_profit))
print('Предприятия, с прибылью ниже среднего значения: ' + ', '.join(companies_with_low_profit))
