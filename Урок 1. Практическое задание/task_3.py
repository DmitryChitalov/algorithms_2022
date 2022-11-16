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


# Способ 1. Cложность: O(n^2)

def my_max(list):  # O(n)
    max = list[0]
    max_index = 0
    for i in range(1, len(list)):  # O(n)
        if list[i] > max:
            max = list[i]
            max_index = i
    return max_index


def top3(dict):  # O(n^2) , так как у нас выполняется цикл внутри цикла.
    keys = list(dict.keys())  # O(len(...))
    values = list(dict.values())  # O(len(...))
    top3 = {}
    for i in range(3):  # O(3)
        max_ind = my_max(values)  # O(n)
        key = keys.pop(max_ind)  # O(n)
        value = values.pop(max_ind)  # O(n)
        top3[key] = value  # O(1)
    return top3


# Способ 2. Cложность: O(n log n)

def top3_2(dict):
    sorted_tuple = sorted(dict.items(), key=lambda x: x[1])  # O(n log n)
    return {k: v for k, v in sorted_tuple[:-4:-1]}  # O(n)


# Способ 3. Cложность: O(n)

def top3_3(dict):
    top3 = {}
    for i in range(3):  # O(3)
        max_num = max(dict.items(), key=lambda k: k[1])  # O(n)
        top3[max_num[0]] = dict.pop(max_num[0])  # O(1)
    return top3


dict = {
    'Google': 50,
    'Yandex': 15,
    'Mail.ru': 10,
    'Audi': 32,
    'BMW': 25
}

print(top3(dict))
print(top3_2(dict))
print(top3_3(dict))
