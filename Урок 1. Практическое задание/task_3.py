"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
Done Please check code below

2) оцените сложность каждого выражения в этих решениях в нотации О-большое
Выполнено Пожалуйста, проверьте O -notation  в коде ниже

3) оцените итоговую сложность каждого решения в нотации О-большое
Выполнено Пожалуйста, проверьте O -notation для обеих функций в коде ниже

4) сделайте вывод, какое решение эффективнее и почему

script    max_values3a       O( N^2 )   более сложен чем
script    max_values3b       O( N )

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def max_values_3a(input_data):                       # O(N^2)
    sorted_data = sorted(input_data.values())       # O(N Log N)
    # print(sorted_data)                            # O(N)
    sorted_dict = {}                                # O(1)
    count = 0                                       # O(1)
    for i in sorted_data[::-1]:                     # O(N)   
        count += 1                                  # O(1)
        if count > 3:                               # O(1)
            break                                   # O(1)
        for k in input_data.keys():                 # O(N)  
            if i == input_data[k]:                  # O(1)
                sorted_dict[k] = input_data[k]       # O(1)
    return sorted_dict                              # O(1)


def max_values_3b(input_data):                       # O(N^2)

    if len(input_data) < 3:                         # O(1)
        raise ValueError("Number of items is less than 3")       # O(1)

#   first 3 pairs
    pair_key = list(input_data.keys())[0]           # O(N)
    pair_value = list(input_data.values())[0]       # O(N)
    pair0 = { pair_key: pair_value}                 # O(1)

    # Debug print
    # print (f' pair0 = {pair0} ')

    pair_key = list(input_data.keys())[1]           # O(N)
    pair_value = list(input_data.values())[1]       # O(N)
    if pair_value > list(pair0.values())[0]:        # O(1)
        pair1 = pair0                               # O(1)
        pair0 = {pair_key: pair_value}              # O(1)
    else:                                           # O(1)
        pair1 = {pair_key: pair_value}             # O(1)

    # Debug print
    # print(f' pair0 = {pair0} ')
    # print(f' pair1 = {pair1} ')

    pair_key = list(input_data.keys())[2]           # O(N)
    pair_value = list(input_data.values())[2]       # O(N)
    if pair_value > list(pair0.values())[0]:         # O(1)
        pair2 = pair1                               # O(1)
        pair1 = pair0                               # O(1)
        pair0 = {pair_key: pair_value}              # O(1)
    elif pair_value>list(input_data.values())[1]:   # O(N)
        pair2 = pair1                               # O(1)
        pair1 = {pair_key: pair_value}              # O(1)
    elif pair_value> list(input_data.values())[2]:  # O(N)
        pair2 = {pair_key: pair_value}              # O(1)

    # Debug print
    # print(f' pair0 = {pair0} ')
    # print(f' pair1 = {pair1} ')
    # print(f' pair2 = {pair2} ')
    # print('\n')

    for i in range(3, len(input_data)):             # O(N)
        # print(f'i = {i}')
        pair_key = list(input_data.keys())[i]       # O(1)
        pair_value = list(input_data.values())[i]   # O(1)

        # Debug print
        # print(pair_key,' ', pair_value)

        pair_key = list(input_data.keys())[i]       # O(N)
        pair_value = list(input_data.values())[i]   # O(N)
        if pair_value > list(pair0.values())[0]:    # O(1)
            pair2 = pair1                           # O(1)
            pair1 = pair0                           # O(1)
            pair0 = {pair_key: pair_value}          # O(1)
        elif pair_value > list(pair1.values())[0]:  # O(N)
            pair2 = pair1                           # O(1)
            pair1 = {pair_key: pair_value}          # O(1)
        elif pair_value > list(pair2.values())[0]:  # O(N)
            pair2 = {pair_key: pair_value}          # O(1)

        # Debug print
        # print(f' pair0 = {pair0} ')
        # print(f' pair1 = {pair1} ')
        # print(f' pair2 = {pair2} ')
        # print('\n')

        pairs = {}                                                  # O(1)
        pairs[list(pair0.keys())[0]] = list(pair0.values())[0]      # O(N)
        pairs[list(pair1.keys())[0]] = list(pair1.values())[0]      # O(N)
        pairs[list(pair2.keys())[0]] = list(pair2.values())[0]      # O(N)

        # Debug print
        # print(f' pairs = {pairs} ')
        # print('\n')

    return pairs                                              # O(1)



if __name__ == '__main__':
    companies = {
        'PapaCarlo': 7,
        'Roga_i_Kopyta': 50,
        'Apple': 45000000,
        'Microsoft': 3700000,
        'Volvo_Tracks': 8300000,
        'Ericsson': 150000,
        'Nokia': 250000,
        'Huwei': 140000
                 }

    print(companies, "\n")
    print(' max_values_3a method')
    print(max_values_3a(companies))
    print('\n max_values_3b method')
    print(max_values_3b(companies))
