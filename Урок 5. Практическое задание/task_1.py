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
несколько вариантов решения этого задания,
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



# Вариант 1 - namedtuple
Companies_templ = namedtuple('Companies', 'prof_quart_1 prof_quart_2 prof_quart_3 prof_quart_4')
TOYOTA = Companies_templ(1000, 2000, 3000, 4000)
MERSEDES = Companies_templ(10000, 25000, 30000, 15000)


def average_profit():
    flag = 1
    companies = []
    companies_up = []
    companies_down =[]
    count = 0
    total = 0
    while flag != '0':
        name_inp = input('Введите название компании: ')
        profits = input('Введите прибыль компании за каждый квартал (4 квартала): ').split()                    #Можно сделать без этого?
        COMPANIES_TEMPL = namedtuple('Companies', 'name prof_quart_1 prof_quart_2 prof_quart_3 prof_quart_4')
        company = COMPANIES_TEMPL(
            name = name_inp,
            prof_quart_1 = int(profits[0]),
            prof_quart_2 = int(profits[1]),
            prof_quart_3 = int(profits[2]),
            prof_quart_4 = int(profits[3])
        )
        companies.append(company)
        total = total + company.prof_quart_1 + company.prof_quart_2 + company.prof_quart_3 + company.prof_quart_4
        count += 4

        flag = input('Для выхода нажмите 0, для продолжения - 1: ')                                             # здесь имя flag - нормальное название по смыслу?
    print(total, count)
    avg = total /count


    for company in companies:
        if company.prof_quart_1 + company.prof_quart_2 + company.prof_quart_3 + company.prof_quart_4 >= avg:
            companies_up.append(company.name)
        else:
            companies_down.append(company.name)

    return avg, companies_up, companies_down

avg = average_profit()
print(f'Среднегодовая прибыль всех компаний: {avg[0]}')
print(f'Компании с годовой прибылью выше средней: {avg[1]}')
print(f'Компании с годовой прибылью ниже средней: {avg[2]}')



# Вариант 2


# def average_profit():                                                                                        # можно делать через рекурсию ?
#     company = input('Введите название компании (в конце введите - 0): ')
#     if company == '0':
#         print('Вы вышли из программы')
#         # расчеты среднего значения и вывод компаний наименований
#
#     else:
#         companies = []
#         profits_inp = input('Введите прибыль компании за каждый квартал (4 квартала) через пробел: ')
#         profits = profits_inp.split()                                                                       #Можно сделать без этого?
#         COMPANIES_TEMPL = namedtuple('Companies', 'prof_quart_1 prof_quart_2 prof_quart_3 prof_quart_4')
#         company = COMPANIES_TEMPL(
#             prof_quart_1 = profits[0],
#             prof_quart_2 = profits[1],
#             prof_quart_3 = profits[2],
#             prof_quart_4 = profits[3]
#         )
#         companies.append(company)
#
#         average_profit()
