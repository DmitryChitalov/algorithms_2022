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


class CompanyProfit():
    def __init__(self):
        self.__company_n = 0
        self.__company_name = []
        self.companies = collections.Counter()

        self.__company_number()
        self.__companies_enter()

    def __company_number(self):
        while True:
            try:
                self.__company_n = int(input('Введите количество предприятий для расчета прибыли: '))
            except ValueError:
                print('Необходимо указать целое число...')
                continue
            break

    def __companies_enter(self):
        for i in range(self.__company_n):
            name = input('Введите название предприятия: ')
            profit = self.__company_profit_enter()
            profit_year = sum(profit)

            d = dict()
            d['profit'] = profit
            d['profit_year'] = profit_year
            self.companies[name] = d

    def __company_profit_enter(self):
        while True:
            try:
                p1, p2, p3, p4 = map(int,
                                     input('через пробел введите прибыль '
                                           'данного предприятия за каждый квартал (Всего 4 квартала): ').split(" "))
            except ValueError:
                print('Необходимо указать 4 целых числа через пробел...')
                continue
            break

        return [p1, p2, p3, p4]

    def company_statistic(self):
        sum_all_companies = 0
        avg_all_companies = 0
        company_profit_u = []
        company_profit_e = []
        company_profit_d = []

        for key, value in self.companies.items():
            sum_all_companies += value['profit_year']
        avg_all_companies = sum_all_companies / len(self.companies.keys())

        for key, value in self.companies.items():
            if value['profit_year'] > avg_all_companies:
                company_profit_u.append(key)
            elif value['profit_year'] < avg_all_companies:
                company_profit_d.append(key)
            else:
                company_profit_e.append(key)

        print('Средняя годовая прибыль всех предприятий:', avg_all_companies)
        print('Предприятия, с прибылью выше среднего значения:', company_profit_u)
        print('Предприятия, с прибылью ниже среднего значения:', company_profit_d)
        print('Предприятия, с прибылью равной среднему значению:', company_profit_e)



if __name__ == '__main__':
    cp = CompanyProfit()
    cp.company_statistic()
