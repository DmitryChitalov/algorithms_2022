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


def count_indicators():

    num = int(input("Введите количество предприятий для расчета прибыли: "))
    company_info = namedtuple("company", "name quarter1 quarter2 quarter3 quarter4")
    companies_stat = {}
    i = num

    while i > 0:
        company = company_info(name=input("Введите название предприятия: "),
                               quarter1=int(input("Введите прибыль данного предприятия за 1 квартал: ")),
                               quarter2=int(input("Введите прибыль данного предприятия за 2 квартал: ")),
                               quarter3=int(input("Введите прибыль данного предприятия за 3 квартал: ")),
                               quarter4=int(input("Введите прибыль данного предприятия за 4 квартал: "))
                               )
        companies_stat[company.name] = (company.quarter1+company.quarter2+company.quarter3+company.quarter4) / 4
        i -= 1

    companies_aver_profit = 0
    for value in companies_stat.values():
        companies_aver_profit += value
    companies_aver_profit = companies_aver_profit / num
    print(f"Средняя годовая прибыль всех предприятий: {companies_aver_profit}")

    companies_aver_profit_more = []
    companies_aver_profit_less = []
    companies_aver_profit_equal = []
    for key, value in companies_stat.items():
        if value < companies_aver_profit:
            companies_aver_profit_less.append(key)
        elif value > companies_aver_profit:
            companies_aver_profit_more.append(key)
        elif value == companies_aver_profit:
            companies_aver_profit_equal.append(key)
    if len(companies_aver_profit_more) > 0:
        result = f"Предприятия, с прибылью выше среднего значения: {companies_aver_profit_more} \n"
    if len(companies_aver_profit_less) > 0:
        result += f"Предприятия, с прибылью ниже среднего значения: {companies_aver_profit_less} \n"
    if len(companies_aver_profit_equal) > 0:
        result += f"Предприятия, с прибылью райной среднему значению: {companies_aver_profit_equal}"
    return result



print(count_indicators())


