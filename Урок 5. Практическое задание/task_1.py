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
за каждый квартал(Всего 4 квартала): 235 345634 55 235 346201

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34 956

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import namedtuple

comp = namedtuple('Company', ' name profit year_profit')
lst_quart = [1, 2, 4, 5]
company = comp(name='123',
               profit=lst_quart,
               year_profit=sum(lst_quart))


class Error(Exception):
    pass


class ToMuchValues(Error):
    pass


class EqualNames(Error):
    pass


def ave_prof(compans):
    sum_prof = 0
    for idx in compans:
        sum_prof += idx.year_profit
    return sum_prof / len(compans)


def more_ave(compans):
    ave = ave_prof(compans)
    return [idx.name for idx in compans if idx.year_profit >= ave]


def less_ave(compans):
    ave = ave_prof(compans)
    return [idx.name for idx in compans if idx.year_profit < ave]


try:
    num_comp = int(input(" Ввведите количество предприятий "))
    comps = []
    for i in range(1, num_comp + 1):
        comp_name = input(f'введите название предприятия {i} : ')
        lst_prof = [int(i) for i in input(
            'Введите значения прибыли за каждый квартал через пробел ').split()]
        if len(lst_prof) != 4:
            raise ToMuchValues

        company = comp(name=comp_name,
                       profit=lst_prof,
                       year_profit=sum(lst_prof)
                       )
        comps.append(company)

    print(f' средняя годовая прибыль всех предприятий {ave_prof(comps)}')
    print('Предприятия, с прибылью выше среднего значения:')
    print(', '.join(map(str, more_ave(comps))))
    print('Предприятия, с прибылью ниже среднего значения:')
    print(', '.join(map(str, less_ave(comps))))
except ValueError:
    print(" Неверные данные ")
except ToMuchValues:
    print("Введено слишком много или слишком мало значений прибыли. Цифры должны быть за 4 квартала")
except EqualNames:
    print("Введены одинаковые имена для нескольких предприятий")
