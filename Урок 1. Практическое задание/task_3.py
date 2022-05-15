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


def find_max_profitable(companies_list: dict, max_count=3) -> list:
    """
    Поиск со сложностью O(n logn)
    """

    companies_sorted_by_profit = dict(
        sorted(companies_list.items(), key=lambda x: x[1], reverse=True))  # O(n logn) + O(n)

    return list(companies_sorted_by_profit.keys())[:max_count]  # O(1) + O(n) + O(max_count)


def find_max_profitable_2(companies_list: dict, max_count=3) -> list:
    """
    Поиск со сложностью O(n)
    На самом деле сложность будет max_count * O(n), но как это верно записать?
    Это решение получилось эффективнее, т.к. O(n) < O(n logn).
    Звучит логично, т.к. в первом варианте идет сортировка, но 1 раз, а здесь поиск максимума, хотя и 3 раза.
    """

    max_profitable = []  # O(1)

    for _ in range(max_count):  # O(3)
        company_with_maximum_profit = max(companies_list, key=companies_list.get)  # O(n)
        companies_list.pop(company_with_maximum_profit, None)  # O(1)
        max_profitable.append(company_with_maximum_profit)  # O(1)

    return max_profitable


if __name__ == '__main__':
    companies = {
        'Intel': 1000,
        'Canon': 2000,
        'Epson': 500,
        'Xerox': 300,
        'HP': 5000
    }

    print(find_max_profitable(companies, 3))
    print(find_max_profitable_2(companies, 3))
