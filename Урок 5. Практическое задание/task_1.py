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
from collections import defaultdict


def enter_information():
    _companies = []
    _lst = ['profit1', 'profit2', 'profit3', 'profit4']

    count = int(input("Введите количество предприятий для расчета прибыли: "))
    for i in range(count):
        name = input("Введите название предприятия: ")
        str_profits = (input("Через пробел введите прибыль данного предприятия за"
                             " каждый квартал(Всего 4 квартала): ")).split()
        int_profits = list(map(int, str_profits))
        Company = namedtuple(name, _lst)
        company = Company(*int_profits)
        _companies.append(company)
    return _companies


def enter_data():
    _companies = defaultdict(int)
    count = int(input("Введите количество предприятий для расчета прибыли: "))
    for i in range(count):
        name = input("Введите название предприятия: ")
        str_profits = (input("Через пробел введите прибыль данного предприятия за"
                             " каждый квартал(Всего 4 квартала): ")).split()
        int_profits = list(map(int, str_profits))
        _companies[name] = int_profits

    return _companies


def get_average_annual_profit(lst_companies):
    result = 0
    for company in lst_companies:
        result += company.profit1 + company.profit2 + company.profit3 + company.profit4
    return result / len(lst_companies)


def calculate_average_annual_profit(def_dct_companies):
    result = 0
    for key, value in def_dct_companies.items():
        result = result + sum(value)

    return result/len(def_dct_companies)


def show_efficiency(lst_companies, limit_value):
    lst_bad = []
    lst_good = []
    lst_average = []
    for company in lst_companies:
        company_annual_profit = company.profit1 + company.profit2 + company.profit3 + company.profit4
        if company_annual_profit < limit_value:
            lst_bad.append(str(company).split('(')[0])
        elif company_annual_profit > limit_value:
            lst_good.append(str(company).split('(')[0])
        else:
            lst_average.append(str(company).split('(')[0])

    if lst_good:
        print(f"Предприятия, с прибылью выше среднего значения: {''.join(lst_good)}")
    if lst_bad:
        print(f"Предприятия, с прибылью ниже среднего значения: {''.join(lst_bad)}")
    if lst_average:
        print(f"Предприятия, с прибылью равной среднему значению: {''.join(lst_average)}")


def show_profitability(def_dct_companies, limit_value):
    lst_bad = []
    lst_good = []
    lst_average = []
    for key, value in def_dct_companies.items():
        company_annual_profit = sum(value)
        if company_annual_profit < limit_value:
            lst_bad.append(key)
        elif company_annual_profit > limit_value:
            lst_good.append(key)
        else:
            lst_average.append(key)

    if lst_good:
        print(f"Предприятия, с прибылью выше среднего значения: {''.join(lst_good)}")
    if lst_bad:
        print(f"Предприятия, с прибылью ниже среднего значения: {''.join(lst_bad)}")
    if lst_average:
        print(f"Предприятия, с прибылью равной среднему значению: {''.join(lst_average)}")


def use_namedtuple():
    companies = enter_information()
    average_annual_profit = get_average_annual_profit(companies)
    print(f"Средняя годовая прибыль всех предприятий: {average_annual_profit}")
    show_efficiency(companies, average_annual_profit)


def use_defaultdict():
    companies = enter_data()
    average_annual_profit = calculate_average_annual_profit(companies)
    print(f"Средняя годовая прибыль всех предприятий: {average_annual_profit}")
    show_profitability(companies, average_annual_profit)


def main():
    use_namedtuple()  # вызвать решение на основе namedtuple
    use_defaultdict()  # вызвать решение на основе defaultdict


if __name__ == "__main__":
    main()
