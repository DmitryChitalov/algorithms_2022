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


def input_data(n):
    while n > 0:
        name_company = input('Введите название предприятия: ')
        profits = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        company_income = namedtuple('company_income', 'company first second third fourth')
        income_company = company_income(
            company=name_company,
            first=profits[0],
            second=profits[1],
            third=profits[2],
            fourth=profits[3]
        )
        profit = [int(income_company[i]) for i in range(1, len(income_company))]
        all_profit.setdefault(income_company[0], sum(profit))
        n -= 1
        return input_data(n)
    return all_profit

def profit_calculation(n):
    profit_calc = input_data(num)
    average_income = sum([v for v in profit_calc.values()]) / num
    above_average = [k for k, v in profit_calc.items() if v >= average_income]
    below_average = [k for k, v in profit_calc.items() if v <= average_income]

    print('Средняя годовая прибыль всех предприятий: ', average_income)
    print('Предприятия, с прибылью выше среднего значения: ', *above_average)
    print('Предприятия, с прибылью ниже среднего значения: ', *below_average)




num = int(input("Введите колличество предприятий для расчета прибыли : "))
all_profit = {}

profit_calculation(num)
