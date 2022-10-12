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

Script listing  - приложен под кодом
"""

from collections import defaultdict


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
    # print(company_profit)

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



# Script listing
#
#  Please enter number of companies for profit calculation : 2
#  Please enter name of company 1 : Roga
#  Please enter quarter profit of company Roga separated by space : 1 2 3 4
#  Please enter name of company 2 : Kopyta
#  Please enter quarter profit of company Kopyta separated by space : 6 7 8 9
#
#  --- Results : ---
#
# Average profit of all companies  :  5.0
# Company Roga has profit = 2.5, that is lower than average
# Company Kopyta has profit = 7.5, that is higher than average
#
# Process finished with exit code 0


