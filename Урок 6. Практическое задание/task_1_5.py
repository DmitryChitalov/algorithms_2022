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

Algoritms lesson5 task_1
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

Script listing  - приложен под кодом

Анализ:
изначально код был написан с использованием словаря company_profit = defaultdict(list)
код был оптимизирован с использованием переменных  Company = recordclass('Company', ('Q1', 'Q2', 'Q3', 'Q4'))

использование памяти:
--- Memory consumption : ---
 getsizeof dict : 240
 asizeof dict : 848

 getsizeof comp1 + comp2 : 96
 asizeof comp1 + comp2 : 96

видна значительная оптимизация памяти при использовании переменных  recordclass
"""

from collections import defaultdict
from recordclass import recordclass
from sys import getsizeof
from pympler.asizeof import asizeof


Company = recordclass('Company', ('Q1', 'Q2', 'Q3', 'Q4'))
comp1 = Company(0, 0, 0, 0)
comp2 = Company(0, 0, 0, 0)

def digit_enter(text_to_enter):
    result_list = []
    while True:
        input_string = input(f'{text_to_enter} : ')
        result_list = list(input_string.split(" "))
        try:
            result_list = list(map(int, result_list))
            return result_list
        except ValueError:
            print(f'Not correct value ')
            continue


def average_total(some_dict):
    sum_of_el = 0
    count_of_el = 0
    for i in some_dict:
        for j in some_dict[i]:
            # print(j)
            sum_of_el +=j
            count_of_el +=1
    print('')
    return sum_of_el/count_of_el


def average_by_comp(some_list):
    sum_of_el = 0
    count_of_el = 0
    for i in some_list:
            sum_of_el += i
            count_of_el += 1
    return sum_of_el/count_of_el


num_companies = digit_enter('\n Please enter number of companies for profit calculation')
num_companies = int(num_companies[0])
company_profit = defaultdict(list)
for i in range (num_companies):
    company_name = input(f' Please enter name of company {i+1} : ')
    company_profit[company_name]
    comment_input = f' Please enter quarter profit of company {company_name} separated by space'
    company_profit[company_name] = digit_enter(comment_input)
    if i == 0:
        comp1.Q1 =  company_profit[company_name][0]
        comp1.Q2 =  company_profit[company_name][1]
        comp1.Q3 =  company_profit[company_name][2]
        comp1.Q4 =  company_profit[company_name][3]
    if i == 1:
        comp2.Q1 =  company_profit[company_name][0]
        comp2.Q2 =  company_profit[company_name][1]
        comp2.Q3 =  company_profit[company_name][2]
        comp2.Q4 =  company_profit[company_name][3]

    print(f' comp1 = {comp1}')
    print(f' comp2 = {comp2}')

    # print(company_profit)
print('\n --- Memory consumption : --- ')

print(f' getsizeof dict : {getsizeof(company_profit)}')
print(f' asizeof dict : {asizeof(company_profit)}')
print(f'\n getsizeof comp1 + comp2 : {getsizeof(comp1) + getsizeof(comp2)}')
print(f' asizeof comp1 + comp2 : {asizeof(comp1) + asizeof(comp2)}')



print('\n --- Results : --- ')
average_profit_total = average_total(company_profit)
print (f'Average profit of all companies  :  {average_profit_total }')



for i in company_profit:
    # print(company_profit[i])
    av_comp= average_by_comp(company_profit[i])
    if av_comp < average_profit_total:
        print(f'Company {i} has profit = {av_comp}, that is lower than average')
    elif av_comp > average_profit_total:
        print(f'Company {i} has profit = {av_comp}, that is higher than average ')
    else:
        print(f'Company {i} has profit = {av_comp}, that is the same as average ')


# script listing:
#
#  Please enter number of companies for profit calculation : 2
#  Please enter name of company 1 : comp1
#  Please enter quarter profit of company comp1 separated by space : 1 2 3 4
#  comp1 = Company(Q1=1, Q2=2, Q3=3, Q4=4)
#  comp2 = Company(Q1=0, Q2=0, Q3=0, Q4=0)
#  Please enter name of company 2 : comp2
#  Please enter quarter profit of company comp2 separated by space : 6 7 8 9
#  comp1 = Company(Q1=1, Q2=2, Q3=3, Q4=4)
#  comp2 = Company(Q1=6, Q2=7, Q3=8, Q4=9)
#
#  --- Memory consumption : ---
#  getsizeof dict : 240
#  asizeof dict : 848
#
#  getsizeof comp1 + comp2 : 96
#  asizeof comp1 + comp2 : 96
#
#  --- Results : ---
#
# Average profit of all companies  :  5.0
# Company comp1 has profit = 2.5, that is lower than average
# Company comp2 has profit = 7.5, that is higher than average
#
# Process finished with exit code 0
