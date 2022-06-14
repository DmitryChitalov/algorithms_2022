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
from collections import defaultdict, namedtuple

# defaultdict


def proceed_analysis(dict_name):
    average_proceed_all = (sum(sum(i) for i in dict_name.values())) / len(dict_name)
    below_avg = []
    above_avg = []
    for key, value in dict_name.items():
        if sum(value) >= average_proceed_all:
            above_avg.append(key)
        else:
            below_avg.append(key)
    return f'Average proceed for all companies: {average_proceed_all}. ' \
           f' Companies with an above-average income: {",".join(above_avg)}, companies with below average income:' \
           f'{",".join(below_avg)}'


def proceed_saver(count=int(input('Enter number of companies: '))):
    companies = defaultdict(int)
    for i in range(count):
        company = input('Enter company: ')
        enter_proceed = input('Enter proceed for each quarter: ')
        companies[company] = [int(i) for i in enter_proceed.split()]
    return print(proceed_analysis(companies))


proceed_saver()

# namedtuple


def proceed_analysis_2(count=int(input('Enter number of companies: '))):
    Proceed_info = namedtuple('Proceed', 'quarter_1 quarter_2 quarter_3 quarter_4')
    Company_name = namedtuple('Company', 'name')
    Full_info = namedtuple('Full_info', ['Company', 'Proceed'])
    all_companies = []
    below_average = []
    above_average = []
    for i in range(count):
        company_name = Company_name(input('Enter company: '))
        _ = input('Enter proceed for each quarter: ')
        proceed_info = Proceed_info(*[int(i) for i in _.split()])
        all_companies.append(Full_info(company_name, proceed_info))

    average_proceed = sum(sum(Full_info.Proceed) for Full_info in all_companies) / count

    for Full_info.Company, Full_info.Proceed in all_companies:
        if sum(Full_info.Proceed) >= average_proceed:
            above_average.append(Full_info.Company.name)
        else:
            below_average.append(Full_info.Company.name)

    return print(f'Average proceed for all companies: {average_proceed}. '\
                 f' Companies with an above-average income: {", ".join(above_average)}, companies with below average income:' \
                 f' {", ".join(below_average)}')


proceed_analysis_2()
