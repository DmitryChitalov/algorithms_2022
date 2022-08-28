"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
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

companies_incomes = {
    'ООО "ООО"': 1,
    'ИП Сахибджонов А.И': 7,
    'Рога и Копыта': 1,
    'Горнопромышленный металлургмческий комбинат': 37,
    'какая-то компания': 9,
    'blablabla': 456

}

def sorted_income1(dict_to_sort): #общее n log n
    sorted_values = set(sorted(dict_to_sort.values())[-3:]) #n log n
    max_values = list(sorted_values) # 1
    max_values.sort() # n log n
    max_values = max_values[::-1] # n
    for i in range(len(max_values)): #1
        for key, val in dict_to_sort.items(): #n
            if val == max_values[i]: #n
                print(f' Компания "{key}" с прибылью {val}')

def sorted_income2(dict_to_sort): # общее n
    list_of_values = []
    max_values_list = []
    for key, val in dict_to_sort.items():
        list_of_values.append(val)
    for _ in range(3):
        i = 1  # (1)
        max_value = max(list_of_values)  # (n)
        #print(max_value)
        max_values_list.append(max_value)
        list_of_values.remove(max_value)
        max_values_list = list(set(max_values_list))
        #print(max_values_list)
    dict_reverse = {}
    for key, val in dict_to_sort.items():
        dict_reverse[val] = key
    #print(dict_reverse)
    i = 0
    dict_to_print = {}
    while True:
        for key, val in dict_reverse.items():
            if key == max_values_list[i]:
                dict_to_print[dict_reverse[key]] = max_values_list[i]
            #print(dict_to_print)
        i += 1
        if i == 3:
            break
    for key, val in dict_to_print.items():
        print(f' Компания "{key}" с прибылью {val}')

sorted_income1(companies_incomes)
print("ы"*50)
sorted_income2(companies_incomes)





#print(a)
#print(dict_to_sort)
#sorted_dict = {}

