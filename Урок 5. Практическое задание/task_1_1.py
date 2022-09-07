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
from collections import defaultdict
from collections import namedtuple
from statistics import mean

MY_DEF_DIC = defaultdict(int)
MY_LST = []
COUNT_FIRM = 0


def input_firms(num_firm):
    if num_firm == 0:
        return MY_DEF_DIC

    inp_firm = input('Введите название предприятия: ')
    ls_profit = input('через пробел введите прибыль данного предприятия \n'
                      'за каждый квартал(Всего 4 квартала): ').split()
    profit = 0
    for _ in ls_profit:
        profit = profit + int(_)
    FIRM = namedtuple(inp_firm, 'id firm_name firm_profit')
    company_data = FIRM(
        id=num_firm,
        firm_name=inp_firm,
        firm_profit=profit
    )
    MY_DEF_DIC[num_firm] = company_data
    num_firm -= 1
    input_firms(num_firm)


def average_profit():
    for key, val in MY_DEF_DIC.items():
        MY_LST.append(val.firm_profit)
    ava_prof = mean(MY_LST)
    return ava_prof


def comparison_with_average(ava_prof):
    print('Средняя годовая прибыль всех предприятий:', ava_prof)
    above_average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit > ava_prof])

    print('Предприятия, с прибылью выше среднего значения:', above_average)
    below_average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit < ava_prof])
    print('Предприятия, с прибылью ниже среднего значения:', below_average)
    average = ' '.join([val.firm_name for val in MY_DEF_DIC.values() if val.firm_profit == ava_prof])
    if average:
        print('Предприятия, с прибылью равной среднему значеню:', average)


if __name__ == '__main__':
    num_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    input_firms(num_firms)

    average_profit()
    comparison_with_average(average_profit())
