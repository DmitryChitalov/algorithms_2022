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

Это файл для пятого скрипта
"""
from memory_profiler import profile
from collections import namedtuple
from recordclass import recordclass
from pympler import asizeof

# Задание 1 Урок 5 алгоритмы


number_enterprises = int(input('Введите количество предприятий: '))
list_companies = []
tuple_companies = namedtuple('Enterprises', 'name_company, quarter_1, quarter_2, quarter_3, quarter_4, sum_years')
result_profit = 0


def data_request(number):
    if number > 0:
        name_company = input('Введите название предприятия:')
        quarter_1 = int(input("Введите прибыль за 1 квартал: "))
        quarter_2 = int(input("Введите прибыль за 2 квартал: "))
        quarter_3 = int(input("Введите прибыль за 3 квартал: "))
        quarter_4 = int(input("Введите прибыль за 4 квартал: "))
        sum_years = quarter_1 + quarter_2 + quarter_3 + quarter_4

        companies = tuple_companies(name_company=name_company,
                                    quarter_1=quarter_1,
                                    quarter_2=quarter_2,
                                    quarter_3=quarter_3,
                                    quarter_4=quarter_4,
                                    sum_years=sum_years)

        list_companies.append(companies)

        return data_request(number - 1)
    else:
        print("данные приняты в обработку ")
        print(list_companies)
        print(f'память - {asizeof.asizeof(list_companies)}')


data_request(number_enterprises)


def average_profit(companies, result):
    for i in companies:
        result += i.sum_years
    result_profit = result / len(companies)
    print(f'Средняя прибыль всех компаний: {result_profit}')

    for i in companies:
        if result_profit > i.sum_years:
            print(f"Предприятия, с прибылью ниже среднего значения:{i.name_company}")
        elif result_profit < i.sum_years:
            print(f"Предприятия, с прибылью выше среднего значения:{i.name_company}")
        else:
            print(f"Предприятия, с прибылью равной среднему значению:{i.name_company}")


average_profit(list_companies, result_profit)

# Готово

number_enterprises = int(input('Введите количество предприятий: '))
list_companies = []
tuple_companies = recordclass('Enterprises', 'name_company, quarter_1, quarter_2, quarter_3, quarter_4, sum_years')
result_profit = 0


def data_request(number):
    if number > 0:
        name_company = input('Введите название предприятия:')
        quarter_1 = int(input("Введите прибыль за 1 квартал: "))
        quarter_2 = int(input("Введите прибыль за 2 квартал: "))
        quarter_3 = int(input("Введите прибыль за 3 квартал: "))
        quarter_4 = int(input("Введите прибыль за 4 квартал: "))
        sum_years = quarter_1 + quarter_2 + quarter_3 + quarter_4

        companies = tuple_companies(name_company=name_company,
                                    quarter_1=quarter_1,
                                    quarter_2=quarter_2,
                                    quarter_3=quarter_3,
                                    quarter_4=quarter_4,
                                    sum_years=sum_years)

        list_companies.append(companies)

        return data_request(number - 1)
    else:
        print("данные приняты в обработку ")
        print(list_companies)
        print(f'память - {asizeof.asizeof(list_companies)}')


data_request(number_enterprises)


def average_profit(companies, result):
    for i in companies:
        result += i.sum_years
    result_profit = result / len(companies)
    print(f'Средняя прибыль всех компаний: {result_profit}')

    for i in companies:
        if result_profit > i.sum_years:
            print(f"Предприятия, с прибылью ниже среднего значения:{i.name_company}")
        elif result_profit < i.sum_years:
            print(f"Предприятия, с прибылью выше среднего значения:{i.name_company}")
        else:
            print(f"Предприятия, с прибылью равной среднему значению:{i.name_company}")


average_profit(list_companies, result_profit)

# Аналитика
# Первый вариант испольнен ввиде namedtuple им занемаймая память - память - 504
# Второй вариант исполнен ввиде recordclass им занемаймая память - память - 216
# Как видим уменьшели занемаймую память больше чем в два раза
