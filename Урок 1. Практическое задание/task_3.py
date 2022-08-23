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
dict_comp = {
    'coca-cola': 200,
    'geekbrains': 12500,
    'apparelle': 23110,
    'navitel': 100,
    'eltex': 2000,
    'zdravcity': 4030,
    'socom': 2209,
    'mi': 5569,
    'cisco': 82901,
    'abibas': 4313
}
#  O(N^2)
def srt_1(dict_comp):
    list_from_dict = list(dict_comp.items()) # O(1)
    for i in range(len(list_from_dict)):     # O(N)
        lowest_value_index = i               # O(1)
        for j in range(i + 1, len(list_from_dict)): # O(N)
            if list_from_dict[j][1] > list_from_dict[lowest_value_index][1]: # O(1)
                lowest_value_index = j # O(1)
        list_from_dict[i], list_from_dict[lowest_value_index] = list_from_dict[lowest_value_index], list_from_dict[i] # O(1)
    print(list_from_dict[0:3]) # O(1)


# O(N*logN)
def srt_2(dict_comp):
    list_from_dict = list(dict_comp.items()) # O(1)
    list_from_dict.sort(key=lambda i: i[1], reverse=True) # O(NLogN)
    for i in range(3): # O(1)
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]}") # O(1)

srt_1(dict_comp)
srt_2(dict_comp)

# Эффективнее второй вариант srt_2 со сложностью O(NLogN)