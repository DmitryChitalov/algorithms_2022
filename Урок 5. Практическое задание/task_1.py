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

number_enterprises = int(input('Введите количество предприятий: '))
list_companies = []
tuple_companies = namedtuple('Enterprises', 'name_company, quarter_1, quarter_2, quarter_3, quarter_4, sum_years')
result_profit = 0


def data_request(number):
    if number > 0:
        name_company = input('Введите название предприятия:')
        quarter_1 = int(input("Введите прибыль за 1 квартал: "))
        quarter_2 = int(input("Введите прибыль за 2 квартал: "))
        quarter_3 = int(input("Введите прибыль за 3 квартал: "))
        quarter_4 = int(input("Введите прибыль за 4 квартал: "))
        sum_years = quarter_1 + quarter_2 + quarter_3 + quarter_4

        companies = tuple_companies(name_company=name_company,
                                    quarter_1=quarter_1,
                                    quarter_2=quarter_2,
                                    quarter_3=quarter_3,
                                    quarter_4=quarter_4,
                                    sum_years=sum_years)

        list_companies.append(companies)

        return data_request(number - 1)
    else:
        print("данные приняты в обработку ")
        print(list_companies)


data_request(number_enterprises)


def average_profit(companies, result):
    for i in companies:
        result += i.sum_years
    result_profit = result / len(companies)
    print(f'Средняя прибыль всех компаний: {result_profit}')

    for i in companies:
        if result_profit > i.sum_years:
            print(f"Предприятия, с прибылью ниже среднего значения:{i.name_company}")
        elif result_profit < i.sum_years:
            print(f"Предприятия, с прибылью выше среднего значения:{i.name_company}")
        else:
            print(f"Предприятия, с прибылью равной среднему значению:{i.name_company}")


average_profit(list_companies, result_profit)







# count_company = int(input("Введите количество предприятий: "))
# name_company = input("Введите название предприятия: ")
# count_profit = 0
# quarter_1st = input("Введите прибыль 1кв: ")
# quarter_2nd = input("Введите прибыль 2кв: ")
# quarter_3rd = input("Введите прибыль 3кв: ")
# quarter_4th = input("Введите прибыль 4кв: ")
# profit_company = []
# profit_company.append(quarter_1st)

name_company = ["Рога", "Копыта"]
company_all = {"Рога": [1, 2, 3, 4], "Копыта": [9, 8, 7, 6]}
x1 = company_all[name_company[0]]
x2 = company_all[name_company[1]]


def averange_profit(new_list):
    result = 0
    for i in new_list:
        result += i
    average_profit = result / 4
    return average_profit


# print(averange_profit(x1))
# print(averange_profit(x2))

result = averange_profit(x1) + averange_profit(x2)
print(result)

