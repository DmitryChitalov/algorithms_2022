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

Enterprise = namedtuple('Enterprise', 'name  sum_year')

enterprise_count = int(input('Введите количество предприятий для анализа: '))
enterprises = [0 for _ in range(enterprise_count)]
#  print(enterprises)
profit_sum = 0

for i in range(enterprise_count):
    name = input(f'Введите название {i + 1}-го предприятия: ')
    quarters = [float(j) for j in input('Введите через пробел прибыль в каждом квартале: ').split()]
    sum_year = sum(quarters)
    # print(sum_year)
    profit_sum += sum_year
    enterprises[i] = Enterprise(name, sum_year)
    print(enterprises[i])

if enterprise_count == 1:
    print(f'Для анализа передано 1 предприятие: {enterprises[0].name} c годовой прибылью: {enterprises[0].sum_year}')

else:
    profit_average = profit_sum / enterprise_count

    less_aver = []
    more_aver = []

    for i in range(enterprise_count):

        if enterprises[i].sum_year < profit_average:
            less_aver.append(enterprises[i])

        elif enterprises[i].sum_year > profit_average:
            more_aver.append(enterprises[i])

    print(f'\nСредняя годовая прибыль всех предприятий: {profit_average: .2f}')

    print(f'Предприятия, чья прибыль меньше среднего{profit_average: .2f}:')
    for ent in less_aver:
        print(f'Предприятие "{ent.name}" с прибылью {ent.sum_year: .2f}')

    print(f'\nПредприятия, чья прибыль больше среднего {profit_average: .2f}:')
    for ent in more_aver:
        print(f'Предприятие "{ent.name}" с прибылью {ent.sum_year: .2f}')

        '''
        

        '''
