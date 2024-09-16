from collections import namedtuple


def calc_and_create_named_tuples(n):
    profit = namedtuple('profit', 'name profit_per_seasons')
    average_profit = {}
    for i in range(n):
        profit_for_comp = profit(
            name=input('Введите название компании'),
            profit_per_seasons=list(map(float,
                                        input('Через пробел введите прибыль данного предприятия'
                                              ' за каждый квартал(Всего 4 квартала):').split(' '))))
        average_profit[profit_for_comp.name] = (
                sum(profit_for_comp.profit_per_seasons) / len(profit_for_comp.profit_per_seasons))
    full_average = sum(average_profit.values())/len(average_profit)
    print(f'Средняя годовая прибыль {full_average}')
    for names in average_profit.keys():
        if average_profit[names] < full_average:
            print(f'Предприятие {names} имеет прибыль ниже средней')
        elif average_profit[names] > full_average:
            print(f'Предприятие {names} имеет прибыль выше средней')
        else:
            print(f'Предприятие {names} имеет прибыль равную средней')


number = int(input('Введите число компаний'))
calc_and_create_named_tuples(number)
