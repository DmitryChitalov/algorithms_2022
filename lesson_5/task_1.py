"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
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

class Profit:
    def __init__(self):
        self.count = int(input('Введите количество предприятий для расчета прибыли: '))
        self.companies = []
        self.sum = 0
        self.all_companies()
        self.result_profit()
        self.compare_profits()

    def company_profit(self):
        name = input('Введите название предприятия: ')
        profits = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        profit_list = profits.split()
        Company = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        self.company = Company(name, int(profit_list[0]), int(profit_list[1]), int(profit_list[2]), int(profit_list[3]))
        return self.company

    def all_companies(self):
        for x in range(self.count):
            self.companies.append(self.company_profit())

    def profit_of_company(self, name):
        self.comp_profit = name.quarter_1 + name.quarter_2 + name.quarter_3 + name.quarter_4
        return self.comp_profit

    def result_profit(self):
        for i in self.companies:
            self.sum += self.profit_of_company(i)
        print(f'Средняя годовая прибыль всех предприятий: {self.sum / self.count}')
        return self.sum

    def compare_profits(self):
        profit_up = 'Предприятия, с прибылью выше среднего значения:'
        profit_down = 'Предприятия, с прибылью ниже среднего значения:'
        for i in self.companies:
            if self.profit_of_company(i) > self.sum / self.count:
                profit_up += f' {i.name},'
            if self.profit_of_company(i) < self.sum / self.count:
                profit_down += f' {i.name},'
        profit_up = profit_up[:-1]
        profit_down = profit_down[:-1]
        print(profit_up)
        print(profit_down)


example = Profit()
