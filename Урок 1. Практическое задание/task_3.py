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


def company_money_first(company_dict):  # O(n log n)
    return sorted(company_dict.items(), key=lambda x: x[1], reverse=True)[:3]  # O(n log n)


def company_money_second(company_list):  # O(n^2)
    start = True  # O(1)
    while start:  # O(n)
        start = False  # O(1)
        for i in range(len(company_list) - 1):  # O(n)
            if company_list[i][1] < company_list[i + 1][1]:  # O(1)
                company_list[i][1], company_list[i + 1][1] = company_list[i + 1][1], company_list[i][1]  # O(1)
                company_list[i][0], company_list[i + 1][0] = company_list[i + 1][0], company_list[i][0]  # O(1)
                start = True  # O(1)
    return company_list[:3]  # O(1)


my_dict = {
    'lukoil': 1000,
    'gazprom': 3000,
    'rosneft': 2000,
    'alrosa': 10000
}

my_list = [
    ['lukoil', 1000],
    ['gazprom', 3000],
    ['rosneft', 2000],
    ['alrosa', 10000]
]

print(company_money_first(my_dict))
print(company_money_second(my_list))

# эффективнее первое решение с использованием встроенной функции sorted(),
# так как линейно-логарифмическая сложность меньше квадратичной
