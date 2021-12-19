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
***
Я сделала больше, чем нужно, т.к., после того, как придумала одно решение, приходили в голову еще. Удалять не стала.
Я считаю, что самое эффективное решение -- пятое, так как у него самая низкая сложность и все решается в одном цикле.
"""

corporations = {'Intel': 5000, 'Google': 7000, 'Yandex': 3000, 'Microsoft': 10000, 'Amazon': 1000}
# 1 O(n log n)
sorted_values = sorted(corporations.values(), reverse=True)  # O(n log n)
sorted_corp = {}  # O(1)
for value in sorted_values:  # O(n)
    for key in corporations.keys():  # O(n)
        if corporations[key] == value:  # O(1)
            sorted_corp[key] = corporations[key]  # O(1)
print(dict(list(sorted_corp.items())[:3]))  # O(2n)

# 2
top_3_corporations = (sorted(corporations.items(), key=lambda items: items[1], reverse=True))[:3]  # O(n log n)
print(top_3_corporations)  # O(1)

# 3 O(2n)
corporations_values = list(corporations.values())  # O(len)
top3_proceeds = []  # O(1)
max_proceeds = corporations_values[0]  # O(1)
for item in corporations_values:  # O(n)
    if item >= max_proceeds:  # O(1)
        top3_proceeds.insert(0, item)  # O(1)
        max_proceeds = item  # O(1)

for key, value in corporations.items():  # O(n)
    if value in top3_proceeds:  # O(n)
        print(key, value)  # O(1)

_corporations_values = corporations_values.copy()

# 4 O(2n)


def max_element(nums_list=_corporations_values):  # O(2n)
    max_item = nums_list[0]  # O(1)
    for item in nums_list:  # O(n)
        if item > max_item:  # O(1)
            max_item = item  # O(1)
    nums_list.pop(nums_list.index(max_item))  # O(n)
    return max_item  # O(1)


i = 0  # O(1)
while i < 3:  # O(1)
    max_elm = max_element()  # O(n)
    for key, value in corporations.items():  # O(n)
        if max_elm == value:  # O(1)
            print(key, value)  # O(1)
            i += 1  # O(1)

# 5 O(n)
max_1 = 0  # O(1)
max_2 = 0  # O(1)
max_3 = 0  # O(1)

for value in corporations.values():  # O(n)
    if value > max_1:  # O(1)
        max_3 = max_2  # O(1)
        max_2 = max_1  # O(1)
        max_1 = value  # O(1)
    elif value > max_2:  # O(1)
        max_3 = max_2  # O(1)
        max_2 = value  # O(1)
    elif value > max_3:  # O(1)
        max_3 = value  # O(1)

print(max_1, max_2, max_3)  # O(1)
