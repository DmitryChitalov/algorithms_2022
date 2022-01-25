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





# Solution 1 : O(n)
"""
print(information_about_companies.values())
print(type(information_about_companies.values()))
print(type(list(information_about_companies.values())))


max_member_of_list = list(information_about_companies.values())[0]


for member in list(information_about_companies.values())[1:]:
    if member > max_member_of_list:
        max_member_of_list = member

print(list(information_about_companies.keys())[list(information_about_companies.values()).index(max_member_of_list)]
      , ":", max_member_of_list)
print(max_member_of_list)


print(list(information_about_companies.keys())[list(information_about_companies.values()).index(max_member_of_list)])

abc = list(information_about_companies.keys())[list(information_about_companies.values()).index(max_member_of_list)]


del information_about_companies
['list(information_about_companies.keys())[list(information_about_companies.values()).index(max_member_of_list)]']


#del information_about_companies[abc]
#print
del information_about_companies[list(information_about_companies.keys())[
    list(information_about_companies.values()).index(max_member_of_list)]]


print(information_about_companies)
"""

def max_annual_profit(dictionary_of_companies_and_profits):

    max_member_of_list = list(dictionary_of_companies_and_profits.values())[0]

    for member in list(dictionary_of_companies_and_profits.values())[1:]:
        if member > max_member_of_list:
            max_member_of_list = member

    print(list(dictionary_of_companies_and_profits.keys())
          [list(dictionary_of_companies_and_profits.values()).index(max_member_of_list)]
          , ":", max_member_of_list)




information_about_companies =\
    {'z': 34534, 'x': 46456, 'y': 987098709, 'a': 1313, 'b': 56857,
     'c': 5232131, 'd': 8973, 'e': 3734, 'f': 980, 'g': 7909}

del dictionary_of_companies_and_profits[list(dictionary_of_companies_and_profits.keys())[
    list(dictionary_of_companies_and_profits.values()).index(max_member_of_list)]]









