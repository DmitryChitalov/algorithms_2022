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


def get_companies(companies_dict: dict):  # O(n log n)

    lst = sorted([[v, k] for k, v in companies_dict.items()], reverse=True)  # проход по словарю O(n)
    # добавление в список O(1)
    # сортировка списка O(n log n)
    print(lst[:3])  # срез O(n)


def get_companies1(companies_dict: dict):  # O(n)

    lst = []  # O(1)
    tmp_companies_dict = dict(companies_dict)  # O(n)
    for i in range(0, 3):  # O(1)
        max_value_list = [0, None]  # O(1)
        for k, v in tmp_companies_dict.items():  # O(n)
            if v > max_value_list[0]:  # O(1)
                max_value_list = [v, k]  # O(1)

        del tmp_companies_dict[max_value_list[1]]  # O(1)
        lst.append(max_value_list)  # O(1)

    print(lst)  # O(1)


if __name__ == '__main__':
    companies = {
        'Ромашка': 10000,
        'Астрал': 20000,
        'РиК': 15000,
        'Позитрон': 5000,
        'Калина': 1000
    }

    get_companies(companies)
    get_companies1(companies)

"""
С точки зрения вычислительной сложности лучшим вариантом будет второй.
"""