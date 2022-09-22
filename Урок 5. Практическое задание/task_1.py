from collections import namedtuple

ntobj = namedtuple('company', 'name profit')
companies = []


def func():
    count = int(input('Введите количество предприятий для расчета прибыли : \n'))

    for x in range(count):
        pname = input('Введите название предприятия : \n')
        spr, smr, atm, wnt = map(int, input('через пробел введите прибыль данного предприятия : \n').split())
        companies.append(ntobj(name=pname, profit=spr+smr+atm+wnt))
    avg_profit = 0
    for x in companies:
        avg_profit += x.profit
    avg_profit /= count

    print(f'Средняя годовая прибыль всех предприятий : {avg_profit}')

    plus = [x.name for x in companies if x.profit > avg_profit]
    minus = [x.name for x in companies if x.profit < avg_profit]
    print('Предприятия, с прибылью выше среднего значения: ', plus)
    print('Предприятия, с прибылью ниже среднего значения: ', minus)


func()