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

from collections import namedtuple, defaultdict


def profit_company_calc():
    """
    Нахождения по нужному количеству компаний
    средней прибыли за квартал и информации больше или меньше
    эта прибыль средней по всем компаниям
    :return: информация о прибыли компаний
    """
    try:
        num_comp = int(input('Введите количество предприятий: '))
    except ValueError:
        return print('Вы ввели не число')
    else:
        my_tuple = namedtuple('info_comp', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        comp_profit = {}
        for i in range(num_comp):
            company_info = my_tuple(
                name=input('Введите название компании: '),
                quarter_1=int(input('Введите прибыль за 1 квартал: ')),
                quarter_2=int(input('Введите прибыль за 2 квартал: ')),
                quarter_3=int(input('Введите прибыль за 3 квартал: ')),
                quarter_4=int(input('Введите прибыль за 4 квартал: ')))
            comp_profit[company_info] = (company_info.quarter_1 + company_info.quarter_2 +
                                         company_info.quarter_3 + company_info.quarter_4) / 4
        total_avr_profit = 0
        for val in comp_profit.values():
            total_avr_profit += val
        total_avr_profit = total_avr_profit / num_comp

        for key, val in comp_profit.items():
            if val < total_avr_profit:
                print(f'У компании {key.name} средняя прибыль {val} ниже среденей '
                      f'по компаниям {total_avr_profit}')
            elif val > total_avr_profit:
                print(f'У компании {key.name} средняя прибыль {val} выше среденей '
                      f'по компаниям {total_avr_profit}')
            else:
                print(f'У компании {key.name} средняя прибыль {val} равна среденей '
                      f'по компаниям {total_avr_profit}')

        return print('Вывод информации завершен')


def profit_company_calc_anothe():
    """
    Нахождения по нужному количеству компаний
    средней прибыли за квартал и информации больше или меньше
    эта прибыль средней по всем компаниям используя defaultdict
    :return: информация о прибыли компаний
    """
    try:
        num_comp = int(input('Введите количество предприятий: '))
    except ValueError:
        return print('Вы ввели не число')
    else:
        comp_profit_avr = defaultdict(int)
        comp_profit = defaultdict(list)
        for i in range(num_comp):
            name = input('Введите название компании: ')
            for j in range(4):
                profit = int(input(f'Введите прибыль за {j + 1} квартал: '))
                comp_profit[name].append(profit)
            comp_profit_avr[name] = sum(comp_profit[name]) / 4
        total_avr_profit = 0
        for val in comp_profit_avr.values():
            total_avr_profit += val
        total_avr_profit = total_avr_profit / num_comp

        for key, val in comp_profit_avr.items():
            if val < total_avr_profit:
                print(f'У компании {key} средняя прибыль {val} ниже среденей '
                      f'по компаниям {total_avr_profit}')
            elif val > total_avr_profit:
                print(f'У компании {key} средняя прибыль {val} выше среденей '
                      f'по компаниям {total_avr_profit}')
            else:
                print(f'У компании {key} средняя прибыль {val} равна среденей '
                      f'по компаниям {total_avr_profit}')

        return print('Вывод информации завершен')


if __name__ == '__main__':
    profit_company_calc()
    profit_company_calc_anothe()
