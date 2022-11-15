"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

"""Решение 2 эффективнее, т.к. ниже О-сложность."""

companies = {'Apple': 7, 'Tesla': 17, 'Intel': 9, 'Ikea': 15, 'Kamaz': 12, 'Volvo': 22, 'Airlines': 16, 'Lada': 1, 'Sony': 13}

"""Общая сложность O(n^4)"""
def solution_1(data):
    values = []  # O(n)
    max_values = []  # O(n)

    for value in data.values():  # O(n)
        values.append(value)  # O(1)

    print("Top 3 companies by solution_1 are:\n")  # O(1)
    for i in range(3):  # O(n)
        max_values.append(max(values))  # O(n)
        values.remove(max(values))  # O(n)
        for k, v in data.items():  # O(n)
            if v == max_values[i]:  # O(1)
                print(f"{k} with a result of {v}.")  # O(1)
    print("\n")
    

""" Общая сложность O(n log n)"""
def solution_2(data):
    sorted_tuple = sorted(data.items(), key=lambda x: x[1], reverse=True)  # O(n log n) - вроде как sorted() O(log n), а перебор у функции O(n)
    sorted_companies = dict(sorted_tuple)  # O(n)

    flag = 3  # O(1)
    print(f"Top {flag} companies by solution_2 are:\n")  # O(1)
    for k, v in sorted_companies.items():  # O(n)
        if flag > 0:  # O(1)
            print(f"{k} with result of {v}.")  # O(1)
            flag -= 1  # O(1)
    print("\n")


solution_1(companies)
solution_2(companies)