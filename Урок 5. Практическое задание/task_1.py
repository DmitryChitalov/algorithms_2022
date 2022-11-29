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
import collections


def companies_info():
    template = collections.namedtuple('company_data', 'id name q1 q2 q3 q4 overall')
    companies = []

    companies_number = int(input("Введите количество предприятий для расчета прибыли: "))

    for i in range(companies_number):
        company_name = input("Введите название предприятия: ")
        company_income = input("Через пробел введите прибыль данного предприятия\nза каждый квартал (Всего 4 квартала): ")
        company_income_list = company_income.split()

        res = template(i,
                       company_name,
                       int(company_income_list[0]),
                       int(company_income_list[1]),
                       int(company_income_list[2]),
                       int(company_income_list[3]),
                       int(company_income_list[0])+int(company_income_list[1])+int(company_income_list[2])+int(company_income_list[3]))

        companies.append(res)

    average = 0
    for company in companies:
        average += company.overall
    average = average / companies_number
    above_average = []
    below_average = []
    for i in companies:
        if i.overall >= average:
            above_average.append(i.name)
        elif i.overall < average:
            below_average.append(i.name)
    return f'Средняя годовая прибыль всех предприятий: {average}\n' \
           f"Предприятия, с прибылью выше среднего значения: {', '.join(above_average)}\n" \
           f"Предприятия, с прибылью ниже среднего значения: {', '.join(below_average)}"


print(companies_info())
