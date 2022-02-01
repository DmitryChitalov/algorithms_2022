"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

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
# Дан список данных по прибыли компаний в формате (год, компания, прибыль)
# Подсчитать налог 13% по каждой компании за 2021 год и для топ 3 компании 
# по прибыли еще добавить налог 5%, отсортировать результат по убыванию налога
# ============= Итоги ==============
# Решение через список списков дало затраты памяти: 24.7148 MiB
# Решение через numpy array дало затраты памяти: 3.5 MiB
# Разница обусловлена тем что array автоматически выбирает размер под объект 
# меньше чем python. Например в данном случае под числа выделено 4 байта


import random
from sys import getsizeof
import numpy as np
from memory_profiler import profile
from collections import defaultdict
from pympler.asizeof import asizeof


companies = []
@profile(precision=4)
def get_comp():
    for i in range(100000):
        year = random.randint(2018, 2021)
        company = (f'comp{i}')
        profit = random.randint(0, 1000000)
        yield tuple([year, company, profit, 0])


@profile(precision=4)
def foo():
    companies = list(get_comp())
    companies = [[c[0], c[1], c[2], c[2]*0.13] for c in companies if c[0] == 2021]
    companies.sort(key=lambda c: c[2], reverse=True)
    companies[:4] = list(map(lambda c: [c[0], c[1], c[2], c[3] + c[2]*0.05], companies[:4]))
    return companies

@profile(precision=4)
def foo2():
    dtype = [('years', int), ('company', 'S10'), ('profit', int), ('tax', int)]
    companies = np.array(list(get_comp()), dtype=dtype)

    filter_2021 = np.in1d(companies['years'], np.array([2021]))
    np_companies_filter = companies[filter_2021]
    np_companies_filter['tax'] = np_companies_filter['profit'] * 0.13
    np_companies_filter
    np_companies_filter = np.sort(np_companies_filter, order='profit')[::-1]
    np_companies_filter['tax'][:4:] = np_companies_filter['profit'][:4:]*0.18
    return np_companies_filter

foo()
foo2()


