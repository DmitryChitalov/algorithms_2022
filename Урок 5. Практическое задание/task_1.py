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
import numpy

from collections import namedtuple


def fill_tuples(count1):
    RES = namedtuple('Company', 'id name avg_inc tot_inc_year')
    incomes = []
    for i in range(0, int(count1)):
        comp_name = input('Введите название предприятия:   ')
        avg_income_list = (input('Через пробел введите прибыль данного предприятия '
                                 'за каждый квартал(Всего 4 квартала): ')).split()
        incoms_list = [int(n) for n in avg_income_list]
        tot = sum(incoms_list)
        lst_avg = numpy.average(incoms_list)
        comp_data = RES(
            id=i,
            name=comp_name,
            avg_inc=lst_avg,
            tot_inc_year=tot
        )
        incomes.append(comp_data)
    return compare_avg(incomes)


def compare_avg(incomes1):
    total_avg_inc = 0
    total_inc = 0

    for income1 in incomes1:
        total_avg_inc += income1.avg_inc
        total_inc += income1.tot_inc_year
    avg_inc1 = total_avg_inc / len(incomes1)
    tot_avg_inc1 = total_inc / len(incomes1)

    big_inc = [income1.name for income1 in incomes1 if income1.avg_inc >= avg_inc1]
    low_inc = [income1.name for income1 in incomes1 if income1.avg_inc < avg_inc1]
    print(f'Средняя годовая прибыль всех предприятий: {tot_avg_inc1}')
    print(f'Предприятия, с прибылью равной или выше среднего значения: {big_inc}')
    print(f'Предприятия, с прибылью ниже среднего значения: {low_inc}')


count = input('Введите количество предприятий для расчета прибыли:   ')
fill_tuples(count)
