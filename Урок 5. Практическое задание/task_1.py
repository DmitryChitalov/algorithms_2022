from collections import namedtuple

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

all_companies = []


def add_to_companies(name: str, income: str):
    """Функция принимает в себя название и прибыль компании, создает объект namedtuple
    и добавляет объект в список компаний"""
    f_q_profit, s_q_profit, th_q_profit, fo_q_profit = list(map(int, (income.split())))
    company = namedtuple(f'{name}', 'company_name f_quarter_profit s_quarter_profit th_quarter_profit fo_quarter_profit')
    new_company = company(company_name=f"{name}", f_quarter_profit=f"{f_q_profit}", s_quarter_profit=f'{s_q_profit}',
                          th_quarter_profit=f'{th_q_profit}', fo_quarter_profit=f'{fo_q_profit}')
    all_companies.append(new_company)
    print(new_company)


def count_profit(companies: list, number_of_c: int):
    """Функция принимает в себя список и количество компаний и возвращает
    среднегодовую прибыль компаний, компании у которых прибыль строго больше среднегодовой и
     список компаний, у которых прибыль строго меньше среднегодовой"""
    full_income = 0
    for x in range(number_of_c):
        full_income += int(companies[x].f_quarter_profit)
        full_income += int(companies[x].s_quarter_profit)
        full_income += int(companies[x].th_quarter_profit)
        full_income += int(companies[x].fo_quarter_profit)
    avg_income = full_income/number_of_c
    over_average = ', '.join([company.company_name for company in companies if int(company.f_quarter_profit) +
            int(company.s_quarter_profit) + int(company.th_quarter_profit)+int(company.fo_quarter_profit) > avg_income])
    under_average = ', '.join([company.company_name for company in companies if int(company.f_quarter_profit) +
            int(company.s_quarter_profit) + int(company.th_quarter_profit)+int(company.fo_quarter_profit) < avg_income])
    return f'Средняя годовая прибыль всех предприятий: {avg_income} \n' \
           f'Предприятия, с прибылью выше среднего значения: {over_average} \n'\
           f'Предприятия, с прибылью ниже среднего значения: {under_average} \n'


# Генератор компаний
"""
import random
number_of_companies = 5
for i in range(number_of_companies):
    random_inc = list(map(str, (random.randint(0, 10000), random.randint(0, 10000),
                            random.randint(0, 10000), random.randint(0, 10000))))
    add_to_companies(f'Horns_{i}', ' '.join(random_inc))
"""

number_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(number_of_companies):
    c_name = input('Введите название предприятия: ')
    c_income = input('Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ')
    add_to_companies(name=c_name, income=c_income)
print(count_profit(all_companies, number_of_companies))

