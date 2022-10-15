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


def calculator():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    companies = namedtuple('company', 'name income')
    avarage_income = {}
    total_avarage_income = 0
    for i in range(n):
        company = companies(name=input('Введите название предприятия: '),
                            income=input('через пробел введите прибыль данного предприятия \
                                         за каждый квартал(Всего 4 квартала): ').split())
        total_income = 0
        for x in range(len(company.income)):
            total_income += int(company.income[x])
        avg_income = total_income / len(company.income)
        avarage_income[company.name] = avg_income
        total_avarage_income += avg_income
    avg_total_avarage_income = total_avarage_income / n
    print(f'Средняя прибыль всех предприятий равна: {avg_total_avarage_income}')
    for key, value in avarage_income.items():
        if value > avg_total_avarage_income:
            print(f'{key} - прибыль выше средней')
        elif value < avg_total_avarage_income:
            print(f'{key} - прибыль ниже средней')
        elif value == avg_total_avarage_income:
            print(f'{key} - прибыль рывна средней')


if __name__ == '__main__':
    calculator()

