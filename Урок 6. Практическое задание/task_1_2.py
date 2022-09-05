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

Это файл для второго скрипта
"""
from collections import namedtuple
from memory_profiler import profile
import random

all_companies = []


def add_to_companies(name: str, income: str):
    """Функция принимает в себя название и прибыль компании, создает объект namedtuple
    и добавляет объект в список компаний"""
    f_q_profit, s_q_profit, th_q_profit, fo_q_profit = list(map(int, (income.split())))
    company = namedtuple(f'{name}', 'company_name f_quarter_profit s_quarter_profit th_quarter_profit fo_quarter_profit')
    new_company = company(company_name=f"{name}", f_quarter_profit=f"{f_q_profit}", s_quarter_profit=f'{s_q_profit}',
                          th_quarter_profit=f'{th_q_profit}', fo_quarter_profit=f'{fo_q_profit}')
    all_companies.append(new_company)


def count_profit(companies: list, number_of_c: int):
    """Функция принимает в себя список и количество компаний и возвращает
    среднегодовую прибыль компаний, компании у которых прибыль строго больше среднегодовой и
     список компаний, у которых прибыль строго меньше среднегодовой"""
    full_income = 0
    for x in range(number_of_c):
        full_income += int(companies[x].f_quarter_profit)
        full_income += int(companies[x].s_quarter_profit)
        full_income += int(companies[x].th_quarter_profit)
        full_income += int(companies[x].fo_quarter_profit)
    avg_income = full_income/number_of_c
    over_average = ', '.join([company.company_name for company in companies if int(company.f_quarter_profit) +
            int(company.s_quarter_profit) + int(company.th_quarter_profit)+int(company.fo_quarter_profit) > avg_income])
    under_average = ', '.join([company.company_name for company in companies if int(company.f_quarter_profit) +
            int(company.s_quarter_profit) + int(company.th_quarter_profit)+int(company.fo_quarter_profit) < avg_income])
    return f'Средняя годовая прибыль всех предприятий: {avg_income} \n' \
           f'Предприятия, с прибылью выше среднего значения: {over_average} \n'\
           f'Предприятия, с прибылью ниже среднего значения: {under_average} \n'


# Генератор компаний
@profile
def com_generator(number_of_companies):
    """Функция создает компании для скрипта"""
    for i in range(number_of_companies):
        add_to_companies(f'Horns_{i}', ' '.join(list(map(str, (random.randint(0, 10000), random.randint(0, 10000),
                                random.randint(0, 10000), random.randint(0, 10000))))))


num_of_companies = 1000
com_generator(num_of_companies)
print(count_profit(all_companies, num_of_companies))


# Генератор компаний
@profile
def com_generator_2(number_of_companies):
    """Функция создает компании для скрипта"""
    for i in range(number_of_companies):
        random_inc = []
        for x in range(4):
            random_inc.append(str(random.randint(0, 10000)))
        add_to_companies(f'Horns_{i}', ' '.join(random_inc))


com_generator_2(num_of_companies)
count_profit(all_companies, num_of_companies)

"""Интересный результат! Передача list comprehensions c ФУНКЦИЕЙ MAP в качестве аргумента функции add_to_companies
увеличил прирост использования оперативной памяти на 0.8  MiB, то есть упростив конструкцию в пользу for
мы можем немного оптимизировать расход памяти"""