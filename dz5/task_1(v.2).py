from collections import namedtuple


def average_profit():
    n = int(input('Введите количество предприятий для расчета прибыли: '))

    def company_tuple(comp, profits):
        res = namedtuple(comp, 'name profit')
        company_profit = res(
            comp,
            profits
        )
        # sum_profit = sum(list(map(int, company_profit.profit.split(' '))))
        return company_profit

    lst_comoany = []
    i = 0
    sum_profit = 0
    while n != i:
        company = input('Введите имя компании: ')
        profit = input('Введите приболь за 4 квартала через пробел: ')
        lst_comoany.append(company_tuple(company, profit))
        i += 1
        sum_profit += sum(list(map(int, profit.split(' '))))
    less = []
    more = []
    for i in lst_comoany:
        comp_sum = sum(list(map(int, i.profit.split(' '))))
        if sum_profit / n > comp_sum:
            less.append(i.name)
        else:
            more.append(i.name)
    return f'Средняя годовая прибыль всех предприятий: {sum_profit / 2},' \
           f' \nПредприятия, с прибылью выше среднего значения: {more},' \
           f' \nПредприятия, с прибылью ниже среднего значения: {less}'


print(average_profit())
