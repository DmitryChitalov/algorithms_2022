"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

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

"""
Задание
Для решения задачи обязательно примените коллекцию из модуля collections
Для своего решнения использовал temp = collections.Counter(temp_firm_revenue)
в строке 47 для подсчета среднего значения. 
Насколько понял вы хотите увидеть решения с namedtuple. Будет сделанно.
"""

"""
Решение 1
def firm_dict(keys, val):
    mas = []
    temp_firm_revenue = {}
    for i in val.split():
        mas.append(int(i))
    temp_firm_revenue[keys] = mas
    temp = collections.Counter(temp_firm_revenue)
    summ = 0
    for i in temp.values():
        summ = sum(i)
    firm_revenue[summ] = temp_firm_revenue


def get_average(ave: dict):
    average_income = sum(ave.keys()) / len(ave)
    print("Средний заработок всех фирм составил ", average_income)
    min_mass = []
    max_mass = []
    for i in ave.keys():
        if average_income > i:
            min_mass.append(ave.get(i))
        else:
            max_mass.append(ave.get(i))
    print("Фирмы с выше средним доходом ", max_mass, " Фирмы с доходом ниже среднего ", min_mass)


firm_revenue = {}

how_many = int(input("Сколько фирм"))

for i in range(how_many):
    key = input("Введите название фирмы")
    val = input("Введите заработок по месяцам через пробел")
    firm_dict(key, val)

print(firm_revenue)
get_average(firm_revenue)

"""

"""
Решение 2 с использованием namedtuple
"""


def pars_string(name_typle):
    profit_firm[(name_typle.first + name_typle.second + name_typle.thirst + name_typle.four) / 2] = name_typle.firm_name


def average_firm():
    ave = 0
    mini = []
    maxi = []
    for i in profit_firm.keys():
        ave = ave + i
    print("Средний доход всех фирм равен ", ave / (len(profit_firm.keys())))
    ave = ave / (len(profit_firm.keys()))

    for i in profit_firm.keys():
        if i > ave:
            maxi.append(profit_firm[i])
        else:
            mini.append(profit_firm[i])
    print("Фирмы с меньшим доходом ", mini, "\nФирмы с доходом больше среднего", maxi)


profit_firm = {}

for i in range(int(input("Введите количество фирм"))):
    Firm = namedtuple("firm", 'frim_name first second thirst four')
    Firm.firm_name = input("Название фирмы")
    Firm.first = int(input("Введите доход за первый месяц"))
    Firm.second = int(input("Введите доход за второй месяц"))
    Firm.thirst = int(input("Введите доход за третий месяц"))
    Firm.four = int(input("Введите доход за четвертый месяц"))
    pars_string(Firm)

average_firm()
