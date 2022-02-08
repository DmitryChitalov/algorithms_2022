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

from collections import namedtuple

count_of_organizations = int(input('Введите количество предприятий для расчета прибыли: '))
organizations = namedtuple('Organizations', 'Name first_quarter second_quarter third_quarter fourth_quarter')

organizations_stat = [
    organizations(input('Введите название предприятия: '), *input('Через пробел введите прибыль данного предприятия за '
                                                                  'каждый квартал(Всего 4 квартала): ').split()) for i
    in range(count_of_organizations)]

organizations_profit = {p[0]: sum(map(int, p[1:])) for p in organizations_stat}
total_profit = sum(organizations_profit.values())
average_total_profit = total_profit / count_of_organizations

below_the_average = [itm for itm in organizations_profit if organizations_profit[itm] < average_total_profit]
above_average = [itm for itm in organizations_profit if organizations_profit[itm] > average_total_profit]

print(f'Средняя годовая прибыль всех предприятий: {average_total_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_the_average}')
