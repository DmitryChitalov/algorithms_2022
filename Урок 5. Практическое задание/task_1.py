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
несколько вариантов решения этого задания,
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

company_count = int(input('Введите количество предприятий для расчета прибыли: '))
OrganizationData = namedtuple('OrganizationData', 'profit1 profit2 profit3 profit4 profit_sum')
company_data = defaultdict(OrganizationData)
company_profit = 0
for i in range(company_count):
    organization_name = input(f'Введите название предприятия ({i + 1}): ')
    while True:
        try:
            organization_profit = list(map(int, input('через пробел введите прибыль данного '
                                                 'предприятия за каждый квартал(Всего 4 квартала): ').split()))
            if len(organization_profit) != 4:
                print('4 значения через пробел')
                raise ValueError()
            break
        except ValueError:
            print('Вы ввели не корректное значение, попробуйте еще раз')

    company_profit += sum(organization_profit)
    organization_profit.append(sum(organization_profit))
    company_data[organization_name] = OrganizationData(*organization_profit)

if company_count <= 0:
    exit(0)

print()

avg_company_profit = company_profit / company_count
print(f'Средняя годовая прибыль всех предприятий: {avg_company_profit}')

company_good, company_bad= [], []

for company, data in company_data.items():
    if data.profit_sum >= avg_company_profit:
        company_good.append(company)
    else:
        company_bad.append(company)

print(f'Предприятия, с прибылью выше среднего значения: {",".join(company_good)}')
print(f'Предприятия, с прибылью ниже среднего значения: {",".join(company_bad)}')
