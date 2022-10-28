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
from collections import namedtuple


companies = namedtuple('Companies', 'id name quarter_1 quarter_2 quarter_3 quarter_4')


def company_money():
    count = int(input("Введите количество предприятий для расчета прибыли: "))
    id = 0
    gen_prof = 0
    avarage_com = {}
    for i in range(count):
        id += 1
        name = input('Введите название предприятия: ')
        year = list(map(int,input("Через пробел введите прибыль данного предприятия"
                                  "за каждый квартал(Всего 4 квартала):").split()))
        company = companies(id, name=name,
                            quarter_1=year[0],
                            quarter_2=year[1],
                            quarter_3=year[2],
                            quarter_4=year[3])
        avarage_com[company.name] = (company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4)
    for i in avarage_com.values():
        gen_prof += i
    gen_prof /= len(avarage_com)

    profit_of_companies_lower_than_average = [i for i, j in avarage_com.items()
                                              if j < gen_prof]
    profit_of_companies_higher_than_average = [i for i, j in avarage_com.items()
                                               if j >= gen_prof]

    return f'Средняя годовая прибыль всех предприятий: {gen_prof}\n' \
           f'Предприятия, с прибылью выше среднего значения: {" ".join(profit_of_companies_higher_than_average)}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {" ".join(profit_of_companies_lower_than_average)}'


print(company_money())