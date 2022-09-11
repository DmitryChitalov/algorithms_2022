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


def ent_profit():
    # Ввод данных о предприятиях и их прибыли:
    enterprises = namedtuple('enterprise', 'ent_name profit_1 profit_2 profit_3 profit_4')
    ent_dict = {}
    ent_count = int(input('Введите количество предприятий: '))
    for _ in range(ent_count):
        ent_name = input(f'Введите название {_ + 1} организации: ')
        ent_dict[ent_name] = enterprises(
            ent_name=ent_name,
            profit_1=int(input(f'Введите доходность {ent_name} в 1 квартале: ')),
            profit_2=int(input(f'Введите доходность {ent_name} во 2 квартале: ')),
            profit_3=int(input(f'Введите доходность {ent_name} в 3 квартале: ')),
            profit_4=int(input(f'Введите доходность {ent_name} в 4 квартале: ')))
    # Расчёт среднегодовой прибыли всех предприятий:
    average_profit = 0
    for enterprise in ent_dict.values():
        average_profit = average_profit + enterprise.profit_1 + \
                         enterprise.profit_2 + enterprise.profit_3 + enterprise.profit_4
    average_profit = average_profit / len(ent_dict)
    # Расчёт годовой прибыли каждой из компаний и их "сортировка":
    ent_high = []
    ent_low = []
    for enterprise in ent_dict.values():
        year_profit = enterprise.profit_1 + enterprise.profit_2 + \
                      enterprise.profit_3 + enterprise.profit_4
        if year_profit > average_profit:
            ent_high.append(enterprise.ent_name)
        else:
            ent_low.append(enterprise.ent_name)
    print(f'Средняя годовая прибыль всех предприятий: {average_profit} \n'
          f'Предприятия, с прибылью выше среднего значения: {ent_high} \n'
          f'Предприятия, с прибылью ниже среднего значения: {ent_low}')


if __name__ == "__main__":
    ent_profit()
