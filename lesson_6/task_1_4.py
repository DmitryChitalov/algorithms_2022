"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы
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
from pympler import asizeof
from collections import namedtuple
from recordclass import recordclass

# def decor(func):
#     def wrapper(*args):
#         m1 = memory_usage()
#         res = func(*args)
#         m2 = memory_usage()
#         mem_diff = m2[0] - m1[0]
#         return res, mem_diff
#     return wrapper


# Исходное решение - задание 5_1 из курса 'Алгоритмы и структуры данных на Python'
# @profile
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
        company = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        self.company = company(name, int(profit_list[0]), int(profit_list[1]), int(profit_list[2]), int(profit_list[3]))
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


# Оптимизированное решение
class Profit2:
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
        company = recordclass('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4')
        self.company = company(name, int(profit_list[0]), int(profit_list[1]), int(profit_list[2]), int(profit_list[3]))
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


if __name__ == '__main__':
    print('Исходное решение')
    example = Profit()
    print('Общий размер объекта при исходном решении: ', asizeof.asizeof(example))  # 928
    print('\nОптимизированное решение')
    example2 = Profit2()
    print('Общий размер объекта при оптимизированном решении: ', asizeof.asizeof(example2))  # 688

''' С целью оптимизации памяти вместо namedtuple из модуля collections был использован модуль recordclass'''
