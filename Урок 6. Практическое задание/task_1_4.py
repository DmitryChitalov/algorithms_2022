"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""

# named tuple
from collections import namedtuple, Counter
from recordclass import recordclass
from pympler.asizeof import asizeof


class Income:
    def __init__(self):
        # self.Company = namedtuple('Company', ['name', 'year_income'])
        self.Company = recordclass('Company', ['name', 'year_income'])
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


if __name__ == "__main__":
    ## namedtuple
    income = Income()
    income.get_companies()
    """
    Заменил namedtuple на recordclass 
    до замены 616 
    поле 424
    """