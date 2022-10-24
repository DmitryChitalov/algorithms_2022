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

company_count = int(input('Введите количество компаний: '))


class Company:
    def __init__(self):
        self.name = input('Введите название компании: ')
        self.profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):')
        self.profit_sum = self.get_sum_profit()
        self.profit_aver = self.profit_sum / 4

    def create_list_of_profits(self):
        return self.profit.split()

    def get_sum_profit(self):
        sum_profit = 0
        profit_list = self.create_list_of_profits()
        for i in profit_list:
            sum_profit += float(i)
        return sum_profit


companies = namedtuple(
    "companies",
    "name sum_profit aver_profit")
ar_companies = {}
for i in range(company_count):
    company = Company()
    ar_companies[i] = companies(name=company.name, sum_profit=company.profit_sum, aver_profit=company.profit_aver)

all_sum_profit = 0

for i in ar_companies:
    print(f'Предприятие: {ar_companies[i].name} прибыль за год - {ar_companies[i].sum_profit}, средняя прибыль'
          f' - {ar_companies[i].aver_profit}')
    all_sum_profit += ar_companies[i].sum_profit

all_sum_aver_profit = all_sum_profit / company_count

print(f'Средняя прибыль за год для всех предприятий {all_sum_aver_profit}')

print('Предприятия, у которых прибыль выше среднего:')
for i in ar_companies:
    if (ar_companies[i].sum_profit > all_sum_aver_profit):
        print(ar_companies[i].name)

print('Предприятия, у которых прибыль ниже среднего:')
for i in ar_companies:
    if (ar_companies[i].sum_profit < all_sum_aver_profit):
        print(ar_companies[i].name)