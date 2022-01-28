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
from collections import defaultdict

def get_num(mess, cycle=True):
    while True:
        try:
            num = int(input(mess))
            break
        except ValueError:
            if not cycle:
                raise
    return num


Profit = namedtuple('profit', ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

Company = namedtuple('company', ['name', 'profit'])

num_companies = get_num("Enter num company: ")

companies = []

for _ in range(num_companies):
    company_name = input('Enter company name: ')
    profits_str = input('Enter profits for 4 quarters: ') 
    profit = Profit(*[int(i) for i in profits_str.split()])
    companies.append(Company(company_name, profit))
      
sum_profit = sum([sum(company.profit) for company in companies])  
avg_profit = sum_profit / len(companies)
print(f'Average annual profit of all companies: {avg_profit}')

sort_companies = defaultdict(list)

for company in companies:
    if sum(company.profit) > avg_profit:
        sort_companies['profit_above_the_average'].append(company)
    elif sum(company.profit) == avg_profit:
        sort_companies['profit_equal_the_average'].append(company)
    else:
        sort_companies['profit_below_the_average'].append(company)

sort_companies_keys_order = ['profit_above_the_average', 'profit_equal_the_average', 'profit_below_the_average']

for sort_key in sort_companies_keys_order:
    if len(sort_companies[sort_key]):
        print(f'Companies with {sort_key}: {[c.name for c in sort_companies[sort_key]]}')
        




# print(f'Average annual profit of all companies: {average_profit}')
# print(f'Companies with profit above the average: {companies_above_avg}')
# print(f'Companies with profit below the average: {companies_below_avg}')


    



