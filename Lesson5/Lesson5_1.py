from collections import namedtuple, defaultdict
from statistics import mean

count = int(input("Введите количество предприятий для расчёта прибыли: "))
i = 0
av_income = {}
while i < count:
    comp_name = input("Введите название предприятия: ")
    comp_income = input("Введите прибыль данного предприятия: ")
    lst = list(comp_income.split())
    lst2 = list(map(int, lst))
    company = namedtuple(comp_name, 'name income')
    COMP = company(name=comp_name, income=lst2)
    av_income[comp_name] = sum(lst2)
    i += 1
# print(min(av_income, key=av_income.get))


print(f'Средняя годовая прибыль всех предприятий: {sum(av_income.values()) / 2}\n'
      f'Предприятия, с прибылью выше среднего значения: {max(av_income, key=av_income.get)}\n'
      f'Предприятия, с прибылью ниже среднего значения: {min(av_income, key=av_income.get)}')
