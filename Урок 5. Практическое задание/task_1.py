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
from statistics import mean


vendor_data = namedtuple('vendors', 'vendor q1 q2 q3 q4 average')


def data_insert(vendors, count=0):  # Функция записи данных (Без расчетов)
    if count >= len(vendors):  # Если данные заполнены выход
        return vendors
    name = input(f' Компания {count + 1}. Введите название предприятия: ')
    profit_sp = input(f' Компания {count + 1}. Через пробел введите прибыль данного '
                       f'предприятияза каждый квартал(Всего 4 квартала):').split()

    try:  # Привидение к типу с плавающей щзапятой, с проверкой на корректность ввода данных.
        profit_sp = [float(i) for i in profit_sp]
    except ValueError:
        print('Ошибка!!! Вы ввели строку вместо числа. Попробуйте еще раз')
        return data_insert(vendors, count)

    if len(profit_sp) != 4:  # Введены ли 4 квартала, или иное кол-во.
        print('Ошибка! Указано не верное кол-во данных. Попробуйте еще раз')
        return data_insert(vendors, count)

    vendors[count] = vendor_data(
        vendor=name,
        q1=profit_sp[0],
        q2=profit_sp[1],
        q3=profit_sp[2],
        q4=profit_sp[3],
        average=mean(profit_sp)
    )
    return data_insert(vendors, count + 1)


def calculation(vendors):  # Расчет средних значений
    profit_max = []  # Список компаний с доходом выше среднего
    profit_min = []  # Список компаний с доходом ниже среднего
    average_by_company = [j.average for i, j in enumerate(vendors)]
    average_total = mean(average_by_company)
    for i in vendors:
        if i.average >= average_total:
            profit_max.append(i.vendor)
        else:
            profit_min.append(i.vendor)
    return f' Компании с прибылью выше среднего: {profit_max} \n Компании с прибылью ниже среднего: {profit_min}'


company_total = int(input('Введите количество предприятий для расчета прибыли: '))
result = data_insert([i for i in range(1, int(company_total) + 1)])
print(calculation(result))
