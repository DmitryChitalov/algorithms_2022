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


def max_income_1(dict_obj):  # Общая сложность O(N^2)
    my_lst = []  # O(1)
    for key in dict_obj:  # O(N)
        my_lst.append([key, dict_obj[key]])  # O(1)
    for i in range(len(my_lst)):  # O(N)
        if my_lst[i][1] > my_lst[0][1]:  # O(1)
            a = my_lst.pop(i)  # O(N)
            my_lst.insert(0, a)  # O(N)
    return my_lst[:3]  # O(1)


def max_income_2(dict_obj): # Общая сложность O(N logN)
    sorted_dict = {}  # O(1)
    my_lst = []  # O(1)
    sorted_income = sorted(dict_obj, key=dict_obj.get, reverse=True)  # O(N logN)
    for i in sorted_income:  # O(N)
        sorted_dict[i] = dict_obj[i]  # O(1)
    for key in sorted_dict:  # O(N)
        my_lst.append([key, sorted_dict[key]])  # O(1)
    return my_lst[:3]  # O(1)


if __name__ == '__main__':

    company_income = {
        'Lukoil': 300,
        'Gazprom': 500,
        'Tatneft': 100,
        'Sberbank': 1000,
        'Apple': 3000
    }

print(max_income_1(company_income))
print(max_income_2(company_income))

"""
Второе решение эффективнее, тк общая сложность решения 1: O(N^2),
а сложность решения 2: O(N logN).
"""