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

companies = {
    'Google': 5000,
    'Yandex': 1500,
    'Magnit': 500,
    'Pyaterochka': 200,
    'Xiaomi': 2300,
    'Apple': 2000,
    'Samsung': 4313
}

def sort_companies_1(companies):  # O(n^2)
    list1 = list(companies.items())
    for x in range(len(list1)):
        lowest_index = x
        for y in range(x+1, len(list1)):
            if list1[y][1] > list1[lowest_index][1]:
                lowest_index = y
        list1[x], list1[lowest_index] = list1[lowest_index], list1[x]
    return(list1[0:3])

def sort_companies_2(companies):  # O(n logn)
    list2 = list(companies.items())
    list2.sort(key=lambda i: i[1], reverse=True)
    return(list2[0:3])


def sort_companies_3(companies):  # O(n)
    list3 = list(companies.items())
    max_list = []
    for i in range(3):
        max_value = max(list3, key=lambda i: i[1])
        list3.remove(max_value)
        max_list.append(max_value)
    return(max_list)

print(sort_companies_1(companies))
print(sort_companies_2(companies))
print(sort_companies_3(companies))