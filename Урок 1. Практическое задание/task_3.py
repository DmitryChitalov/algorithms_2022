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


info_data = {
    "Yotube": 278657156,
    "Twitch": 478956521,
    "Rutube": 14789652,
    "Google": 998627556,
    "Apple": 862357415,
    "Samsung": 79866325,
    "Alpine": 78456321,
    "Ikea": 569873256,
    "Blackberry": 147963256,
    "Discord": 14587125,

}


def best(data_dict):
    """
    O(n log n)
    """
    list_data = list(data_dict.items())               # O(n)
    list_data.sort(key=lambda i: i[1], reverse=True)  # O(n log n)
    return list_data[:3]                              # O(1)


def best_2(data_dict):
    """
    O(n)
    """
    top_3 = {}                                  # O(1)
    data_copy = data_dict.copy()                # O(n)
    for i in range(3):                          # O(1)
        max_value = 0                           # O(1)
        max_key = 0                             # O(1)
        for key in data_copy.keys():            # O(n)
            if data_copy[key] > max_value:      # O(1)
                max_value = data_copy[key]      # O(1)
                max_key = key                   # O(1)
        top_3[max_key] = max_value              # O(1)
        data_copy.pop(max_key)                  # O(1)
    return top_3                                # O(1)


print(best(info_data))
print(best_2(info_data))
