"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

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


# Первый вариант через namedtuple
n = int(input('Введите кол-во предприятий: '))
CompanyClass = namedtuple('Company', 'name first second third firth')
companies = []

for _ in range(n):
    try:
        companies.append(CompanyClass(
                    name=input('Название компании '),
                    first=float(input('Первая четверть: ')),
                    second=float(input('Вторая четверть: ')),
                    third=float(input('Третья четрветь: ')),
                    firth=float(input('Четвертая четверть: '))
                    ))
    except:
        print('Введены неверные данные. ')

# Считаем среднюю прибыль
avg_all = 0
for i in companies:
    avg_all += sum(i[1:])

avg_all = avg_all / n
print(f'Средняя прибыль всех компаний: {avg_all:.2f}')

high_avg = [(x.name, sum(x[1:])) for x in companies if sum(x[1:]) > avg_all]
print('Компании с доходом выше среднего', high_avg)

low_avg = [(x.name, sum(x[1:])) for x in companies if sum(x[1:]) < avg_all]
print('Компании с доходом ниже среднего', low_avg)


# Второй вариант через словарь
n = int(input('Введите кол-во предприятий: '))
companies_dict = {}

for _ in range(n):
    _name = input('Введите название компании: ')
    try:
        companies_dict[_name] = [int(input('Первая четверть: ')),
                                 int(input('Вторая четверть: ')),
                                 int(input('Третья четрветь: ')),
                                 int(input('Четрветая четрветь: '))]
    except:
        print('Введены неверные данные. ')

avg_all = sum([sum(x) for x in companies_dict.values()]) / n
print(f'Средняя прибыль всех компаний: {avg_all:.2f}')


high_avg = []
for k, v in companies_dict.items():
    if sum(v) > avg_all:
        high_avg.append((k, sum(v)))
print('Компании с доходом выше среднего', high_avg)


low_avg = []
for k, v in companies_dict.items():
    if sum(v) < avg_all:
        low_avg.append((k, sum(v)))
print('Компании с доходом ниже среднего', low_avg)
