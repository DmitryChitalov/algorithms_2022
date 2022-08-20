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

""" 
Примечание. Сортировка не позволяет изменять порядок словаря на месте.
Записываем упорядоченные пары в совершенно новый пустой словарь.
В Python 3.7 и более поздних версиях словари сортируются по порядку
вставки элементов. В более ранних версиях они были неупорядоченными.
"""
def max_profits_1(companies, count):
    """Функция должная вернуть минимальное значение для списка.
    Sort the values

    Сложность: O(N^2)
    """
    sorted_values = sorted(companies.values(), reverse=True)
    li = []
    [li.append(x) for x in sorted_values if x not in li]
    li = li[:count]
    sorted_dict = {}

    for i in li:
        if count == 0:
            break
        for k in companies.keys():
            if companies[k] == i:
                sorted_dict[k] = companies[k]
                count = count - 1
                if  count == 0:
                    break

    return sorted_dict


def max_profits_2(companies, count):
    """Функция должная вернуть минимальное значение для списка.
    Sort the values

    Сложность: O(NlogN)
    """
    sorted_dict = {}
    # список ключей, отсортированных по убыванию
    sorted_keys = sorted(companies, key=companies.get, reverse=True)
    sorted_keys = sorted_keys[:count]

    for i in sorted_keys:
        sorted_dict[i] = companies[i]

    return sorted_dict


companies1 = {'A': 10, 'B': 50, 'C': 30, 'D': 20, 'E': 40, 'F': 50, 'G': 30 }
print(max_profits_1(companies1, 4))
print(max_profits_2(companies1, 5))
