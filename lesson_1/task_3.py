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

# 1) O(n^2)
def sort_companies_1(companies):
    list1 = list(companies.items())  # O(n)
    for x in range(len(list1)):  # 0(n)
        lowest_index = x  # 0(1)
        for y in range(x+1, len(list1)):  # 0(n)
            if list1[y][1] > list1[lowest_index][1]:  # O(1)
                lowest_index = y  # O(1)
        list1[x], list1[lowest_index] = list1[lowest_index], list1[x]  # O(1)
    return(list1[0:3])  # 0(1)

# 2) O(n logn)
def sort_companies_2(companies):
    list2 = list(companies.items())  # O(n)
    list2.sort(key=lambda i: i[1], reverse=True)  # O(n logn)
    return(list2[0:3])  # 0(1)

# 3) O(n)
def sort_companies_3(companies):
    list3 = list(companies.items())  # O(n)
    max_list = []  # O(1)
    for i in range(3):  # O(1)
        max_value = max(list3, key=lambda i: i[1])  # O(n)
        list3.remove(max_value)  # O(n)
        max_list.append(max_value) # O(1)
    return(max_list)  # 0(1)

print(sort_companies_1(companies))
print(sort_companies_2(companies))
print(sort_companies_3(companies))

# Третье решение самое эффективное, так как имеет самую низкую сложность из всех трех решений (линейную).