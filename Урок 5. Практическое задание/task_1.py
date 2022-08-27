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

num = int(input('Введите количество предприятий для расчета прибыли'))
stats = namedtuple('company', 'name q1 q2 q3 q4')
common = dict()

for i in range(num):
    try:
        data = stats(
            name=input('Введите название предприятия'),
            q1=int(input('Введите прибыль за первый квартал')),
            q2=int(input('Введите прибыль за второй квартал')),
            q3=int(input('Введите прибыль за третий квартал')),
            q4=int(input('Введите прибыль за четвертый квартал'))
        )
        avg_prof = (data.q1 + data.q2 + data.q3 + data.q4) / 4
        common[data.name] = avg_prof

    except ValueError:
        break

common_avg = 0
for i in common.keys():
    common_avg = common_avg + common[i]

common_avg = common_avg / num
print(f'Средняя прибыль предприятий - {common_avg}')

for i in common.keys():
    if common[i] < common_avg:
        print(f'Предприятие {i} имеет прибыль ниже средней')
    if common[i] > common_avg:
        print(f'Предприятие {i} имеет прибыль выше средней')
    if common[i] == common_avg:
        print(f'Предприятие {i} имеет среднюю прибыль')
