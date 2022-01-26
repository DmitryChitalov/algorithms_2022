from collections import defaultdict

companies = defaultdict(float)


def companies_calculations():
    general_average_profit = 0

    num_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))

    for i in range(num_of_companies):
        name = input('Введите название предприятия: ')
        quarter_1 = float(input('Введите прибыль за первый квартал: '))
        quarter_2 = float(input('Введите прибыль за второй квартал: '))
        quarter_3 = float(input('Введите прибыль за третий квартал: '))
        quarter_4 = float(input('Введите прибыль за четвертый квартал: '))

        average_profit = (quarter_1 + quarter_2 + quarter_3 + quarter_4) / 4

        companies[name] = average_profit
        general_average_profit += average_profit

    profit_of_companies_lower_than_average = [i for i, j in companies.items()
                                              if j < general_average_profit / 4]
    profit_of_companies_higher_than_average = [i for i, j in companies.items()
                                               if j >= general_average_profit / 4]

    return f'Предприятия, с прибылью выше или = среднего значения: {profit_of_companies_higher_than_average}\
             Предприятия, с прибылью ниже среднего значения: {profit_of_companies_lower_than_average}'


print(companies_calculations())
