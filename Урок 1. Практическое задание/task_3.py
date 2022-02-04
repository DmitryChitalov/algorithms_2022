"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


#  Solution 1 : O(n)


def max_annual_profit_1(dictionary_of_companies_and_profits):  # Линейная Сложность:O(n)

    max_member_of_list = list(dictionary_of_companies_and_profits.values())[0]  # Константная Сложность:O(1)

    for member in list(dictionary_of_companies_and_profits.values())[1:]:  # Линейная Сложность:O(n)
        if member > max_member_of_list:  # Константная Сложность:O(1)
            max_member_of_list = member  # Константная Сложность:O(1)

    print(list(dictionary_of_companies_and_profits.keys())
          [list(dictionary_of_companies_and_profits.values()).index(max_member_of_list)]
          , ":", max_member_of_list)  # Линейная Сложность:O(n)

    del dictionary_of_companies_and_profits[list(dictionary_of_companies_and_profits.keys())[
     list(dictionary_of_companies_and_profits.values()).index(max_member_of_list)]]  # Линейная Сложность:O(n)


information_about_companies_1 =\
    {'z': 34534, 'x': 46456, 'y': 987098709, 'a': 1313, 'b': 56857,
     'c': 5232131, 'd': 8973, 'e': 3734, 'f': 980, 'g': 7909}


max_annual_profit_1(information_about_companies_1)
max_annual_profit_1(information_about_companies_1)
max_annual_profit_1(information_about_companies_1)


#  Solution 2 : Сложность типа O(n**4)


def allocation_of_n_maximum_values_of_list(lst, number):  # Квадратичная Сложность:O(n**2)
    list_of_maximum_n_values = []  # Константная Сложность:O(1)
    for i in range(number):  # Линейная Сложность:O(n)
        max_member_of_list = lst[0]  # Константная Сложность:O(1)
        for member in lst[1:]:  # Линейная Сложность:O(n)
            if member > max_member_of_list:  # Константная Сложность:O(1)
                max_member_of_list = member  # Константная Сложность:O(1)
        list_of_maximum_n_values.append(max_member_of_list)  # Константная Сложность:O(1)
        lst.remove(max_member_of_list)  # Линейная Сложность:O(n)
    return list_of_maximum_n_values  # Константная Сложность:O(1)


def defining_dictionary_keys_by_values(dictionary, lst):  # Квадратичная Сложность:O(n**2)
    for member in lst:  # Линейная Сложность:O(n)
        for key, value in dictionary.items():  # Линейная Сложность:O(n)
            if member == value:  # Константная Сложность:O(1)
                print(key, ':', value)  # Константная Сложность:O(1)


information_about_companies_2 =\
    {'h1': 57898, 'z1': 34534, 'x1': 46456, 'y1': 980987, 'a1': 1313, 'b1': 56857,
     'j1': 5232131, 'd1': 8973, 'e1': 3734, 'f1': 980, 'g1': 7909, 'z2': 456}


defining_dictionary_keys_by_values(information_about_companies_2,
                                   allocation_of_n_maximum_values_of_list(list(information_about_companies_2.values())
                                                                          , 3))


"""
Решение номер 1 является более эффективным, потому что о-нотация такого решения линейная, и , поэтому,
 по сравнению со вторым решением,  при увеличении объёма входных данных , потребуется меньше времени для достижения
 результата.
 Но во втором решениии содержатся функции, которые могут быть полезны при решении лругих задач. 
"""

