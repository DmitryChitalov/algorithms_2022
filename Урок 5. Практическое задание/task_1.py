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


def get_company_list():
    Company = namedtuple('company', "name, income")
    n = input("Введите количество предприятий для расчета прибыли: ")
    company_list = list()
    for i in range(int(n)):
        name = input('Введите название предприятия: ')
        income = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').strip(
            ' ')
        all_income = sum(list(map(int, income.split(' '))))
        company_list.append(Company(name, all_income))
    return company_list


def avg_income(company_list):
    return sum([i.income for i in company_list]) / len(company_list)


def div_income(company_list, avg):
    more = list()
    lower = list()
    for i in company_list:
        if i.income < avg:
            lower.append(i.name)
        else:
            more.append(i.name)
    return more, lower


if __name__ == "__main__":
    company_list = get_company_list()
    avg_income = avg_income(company_list)
    div_income = div_income(company_list, avg_income)

    print(f'Средняя годовая прибыль всех предприятий: {avg_income}\n'
          f'Предприятия, с прибылью выше среднего значения: {", ".join(div_income[0])} \n'
          f'Предприятия, с прибылью ниже среднего значения: {", ".join(div_income[1])}')
