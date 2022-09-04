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

data_storage = {
    "Avito": 6713661,
    "Wildberries": 3671650226,
    "Ozon": 3254165,
    "Yandex": 3541066,
    "Gazprom": 682654,
    "Rosteh": 6871466,
    "Marvel": 6574416,
    "Softline": 75169159,
    "Huawei": 1489905,
    "Rostelecom": 14587125,
    "Kaspersky": 459665497,
    "Cisco Systems": 78945613,
    "Sytronics Group": 123852963,
    "Umbrella": 7418529633,
    "Tegrus": 987456321,
    "Allegro": 369852147,
    "Invent": 4561258,
    "Flowers": 32547861,
    "Olymp": 45876321,
    "WorldPress": 78254122
}


def winners(data_dict):
    """
    Сложность: O(n log n)
    """
    list_data = list(data_dict.items())               # O(n)
    list_data.sort(key=lambda i: i[1], reverse=True)  # O(n log n)
    return list_data[:3]                              # O(1)


def winners_2(data_dict):
    """
    Сложность:  O(n)
    """
    top_3 = {}                                  # O(1)
    data_copy = data_dict.copy()                # O(n)
    for _ in range(3):                          # O(1)
        max_value = 0                           # O(1)
        max_key = 0                             # O(1)
        for key in data_copy.keys():            # O(n)
            if data_copy[key] > max_value:      # O(1)
                max_value = data_copy[key]      # O(1)
                max_key = key                   # O(1)
        top_3[max_key] = max_value              # O(1)
        data_copy.pop(max_key)                  # O(1)
    return top_3                                # O(1)


print(winners(data_storage))
print(winners_2(data_storage))
