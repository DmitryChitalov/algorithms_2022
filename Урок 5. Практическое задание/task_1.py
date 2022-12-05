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
# named tuple
from collections import namedtuple, Counter


class Income:
    def __init__(self):
        self.Company = namedtuple('Company', ['name', 'year_income'])
        self.companies = []

    def get_companies(self):
        """
        Здесь мы получаем доход за год и добовляем экземпляр компании (имя + доход) в список компаний
        """
        # количество компаний
        amount = int(input('Input amount of companies for calculation : '))

        while amount:
            amount -= 1

            name = input('enter company name : ')

            # получаю доход компании за 4 четверти и переобразую их в число
            income = map(lambda x: int(x), input('Enter company income for quarter separated by space : ').split(' '))
            # считаю доход за годl
            year_income = sum(income)
            # создаю экземпляр именнованого кортежа с именем компании
            company = self.Company(name=name,
                                   year_income=year_income)

            self.companies.append(company)

    def get_average(self):
        """
        получает средний доход окмпаний
        """
        total_income = 0
        # достаю доход каждой компании
        for company in self.companies:
            total_income += company.year_income
        # получаю средний доход
        try:
            average = total_income / len(self.companies)
        except ZeroDivisionError:
            average = 0
        return average

    def show_statistic(self):
        """
        получаю компании выше и ниже среднего дохода
        """
        average = self.get_average()
        stats = {'over': [],
                 'less': [],
                 'average': average}

        for company in self.companies:
            if company.year_income >= average:
                stats['over'].append(company.name)
            else:
                stats['less'].append(company.name)

        return stats

    def __str__(self):
        stats = self.show_statistic()
        text = f"Average income {stats['average']}\n" \
               f"Companies with income over average : {', '.join(stats['over'])}\n" \
               f"Companies with income less than average {', '.join(stats['less'])}"
        return text


# Collections
def get_companies():
    """
    Получает компании и доход
    :return: Counter с именами компаний и доходом за год
    """
    companies = Counter()
    amount = int(input('Input amount of companies for calculation : '))
    for i in range(amount):
        name = input('Please enter name of the company : ')
        income = map(lambda x: int(x), input('Enter company income for quarter separated by space : ').split(' '))
        companies[name] = sum(income)

    return companies


# 1 1 1 1
def get_stats(companies: Counter):
    average = sum(companies.values()) / len(companies)
    over = []
    less = []
    for company, income in companies.items():
        if income >= average:
            over.append(company)
        else:
            less.append(company)

    text = f"""
    Average income : {average}
    Companies with income over average : {", ".join(over)}
    Companies with income less than average {", ".join(less)} 
    """
    return text


def main():
    companies: Counter = get_companies()
    print(get_stats(companies))


if __name__ == "__main__":
    ## namedtuple
    income = Income()
    income.get_companies()
    print(income)
    ## Collections
    main()
