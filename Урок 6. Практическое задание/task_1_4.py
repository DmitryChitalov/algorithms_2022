"""
Задание 1.

Это файл для четвертого скрипта
"""
"""
Урок 5
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
"""


import sys
from collections import namedtuple
from recordclass import recordclass


def enter_comp():
    comp_name = input('Введите название компании: ')
    quarters = list(map(int, input('Через пробел введите прибыль данного \
предприятия за каждый квартал(Всего 4 квартала): ').split()))
    aver_val = sum(quarters) / 4
    comp_parts = COMP(
        id=i,
        comp_name=comp_name,
        quarter1=quarters[0],
        quarter2=quarters[1],
        quarter3=quarters[2],
        quarter4=quarters[3],
        aver_val=aver_val
    )
    print(sys.getsizeof(comp_parts))
    return comp_parts


n = int(input('Введите количество компаний: '))
glob_aver_val = 0
companes = []
COMP = namedtuple('Comp', 'id comp_name quarter1 quarter2 quarter3 quarter4 aver_val')
# COMP = recordclass('Comp', 'id comp_name quarter1 quarter2 quarter3 quarter4 aver_val')

for i in range(1, n+1):
    companes.append(enter_comp())
    glob_aver_val += companes[i-1].aver_val

glob_aver_val = glob_aver_val / n
print('-' * 100)
print(f'Средняя годовая прибыль всех предприятий: {glob_aver_val}')

print('Предприятия, с прибылью выше либо равной среднего значения: ', end=' ')
for i in companes:
    if i.aver_val >= glob_aver_val:
        print(i.comp_name, end=' ')

print('\n', 'Предприятия, с прибылью выше среднего значения: ', sep='', end=' ')
for i in companes:
    if i.aver_val < glob_aver_val:
        print(i.comp_name, end=' ')

'''
72 - recordclass
96 - namedtule
При замене namedtule на recordclass объем занимаемой памяти уменьшился
'''