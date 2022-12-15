import collections
import random


def sum_tuple(numbers):
    '''tuple --> sum'''

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4'])

base_enterprise = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_enterprise[name] = Enterprise(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

base_enterprise['Name1'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

base_enterprise['Name2'] = Enterprise(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

total_profit = ()

for name, profit in base_enterprise.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_enterprise)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_enterprise.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in base_enterprise.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')