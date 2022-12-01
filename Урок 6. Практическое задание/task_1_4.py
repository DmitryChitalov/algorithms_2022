"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""

from collections import defaultdict
from statistics import mean
from pympler import asizeof
from recordclass import recordclass

# задание из курса алгоритмы и структуры данных


number_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
my_dict = defaultdict(int)

for i in range(number_of_companies):
    company_name = input('Введите название предприятия: ')
    profit = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    my_dict[company_name] = mean([int(el) for el in profit.split(" ")])

total_profit = round(mean(my_dict.values()), 3)
print(f'Размер: {asizeof.asizeof(profit + company_name)}')
print(f"Средняя годовая прибыль всех предприятий: {total_profit}.")
print(f"Предприятия, с прибылью выше среднего значения: "
      f"{', '.join([el for el in my_dict.keys() if my_dict[el] > total_profit])}.")
print(f"Предприятия, с прибылью ниже среднего значения: "
      f"{', '.join([el for el in my_dict.keys() if my_dict[el] < total_profit])}.")


def average_annual_income_1():
    count = int(input('Введите количество предприятий для расчета прибыли: '))
    INFO = recordclass('Company', 'name income')
    aver_ann_inc = {}
    total_aver = 0
    higher_inc = []
    lower_inc = []
    aver_inc = []
    for i in range(count):
        COMP_INFO = INFO(
            name=input('Введите название предприятия: '),
            income=input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        )
        print(f'Размер recordclass: {asizeof.asizeof(COMP_INFO)}')
        aver_ann_inc[COMP_INFO.name] = \
            (int(COMP_INFO.income.split(' ')[0]) + int(COMP_INFO.income.split(' ')[1])
             + int(COMP_INFO.income.split(' ')[2]) + int(COMP_INFO.income.split(' ')[3])) / 4

    for val in aver_ann_inc.values():
        total_aver += val
    total_aver = total_aver / count

    print(f'Средняя годовая прибыль всех предприятий: {total_aver}')

    for k, v in aver_ann_inc.items():
        if v > total_aver:
            higher_inc.append(k)
        elif v < total_aver:
            lower_inc.append(k)
        else:
            aver_inc.append(k)


average_annual_income_1()

# надеюсь я не ошибся когда вставлял расчеты. после замеров, при использовании recordclass размера пямяти был в 2 раза меньше
