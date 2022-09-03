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
from collections import namedtuple, defaultdict


# namedtuple
def get_company():
    name = input('Введите название предприятия: ')
    profit_quarters = input('Через пробел ввидите прибыль данного предприятия '
                            'за каждый квартал (всего 4 квартала): ').split()
    profit_year = sum(map(float, profit_quarters))
    return name, profit_year


def namedtuple_calc():
    CompanyInfo = namedtuple('CompanyInfo', 'name profit')
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    company_list = [CompanyInfo(*get_company()) for _ in range(count)]
    mean_val = sum(map(lambda x: x.profit, company_list)) / count
    print('Предприятия, с прибылью выше среднего значения:', end=' ')
    print(*(el.name for el in company_list if el.profit >= mean_val), sep=', ')
    print('Предприятия, с прибылью ниже среднего значения:', end=' ')
    print(*(el.name for el in company_list if el.profit < mean_val), sep=', ')


# defaultdict
def defaultdict_calc():
    company_dict = defaultdict(float)
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    for _ in range(count):
        name = input('Введите название предприятия: ')
        for quarter in range(1, 5):
            profit_quarter = float(input(f'Введите прибыль за {quarter} квартал: '))
            company_dict[name] += profit_quarter
    mean_val = sum(company_dict.values()) / count
    print('Предприятия, с прибылью выше среднего значения:', end=' ')
    print(*(key for key, val in company_dict.items() if val >= mean_val), sep=', ')
    print('Предприятия, с прибылью ниже среднего значения:', end=' ')
    print(*(key for key, val in company_dict.items() if val < mean_val), sep=', ')


if __name__ == '__main__':
    print('1) namedtuple', '\n')
    namedtuple_calc()
    print('\n', '2) defaultdict', '\n')
    defaultdict_calc()
