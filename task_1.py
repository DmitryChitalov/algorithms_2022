from collections import namedtuple

companies = namedtuple('Companies', 'id name quarter_1 quarter_2 quarter_3 quarter_4')


def companies_calculations():
    id = 0
    average_profit_of_companies = {}
    general_profit = 0

    num_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))

    while id < num_of_companies:
        id += 1
        company = companies(id, name=input('Введите название предприятия: '),
                            quarter_1=int(input('Введите прибыль за первый квартал: ')),
                            quarter_2=int(input('Введите прибыль за второй квартал: ')),
                            quarter_3=int(input('Введите прибыль за третий квартал: ')),
                            quarter_4=int(input('Введите прибыль за четвертый квартал: '))
                            )
        average_profit = (company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4) / 4
        average_profit_of_companies[company.name] = average_profit

    for i in average_profit_of_companies.values():
        general_profit += i

    profit_of_companies_lower_than_average = [i for i, j in average_profit_of_companies.items()
                                              if j < general_profit / 4]
    profit_of_companies_higher_than_average = [i for i, j in average_profit_of_companies.items()
                                               if j >= general_profit / 4]

    return f'Предприятия, с прибылью выше или = среднего значения: {profit_of_companies_higher_than_average}\
            Предприятия, с прибылью ниже среднего значения: {profit_of_companies_lower_than_average}'


print(companies_calculations())
