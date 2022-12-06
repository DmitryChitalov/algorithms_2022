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


profit_company = {'Netflix': 1500, 'Microsoft': 8000, 'Intel': 5800, 'Tesla': 9400, 'NVIDIA': 6000}


# Способ №1
# Сложность O(n log n)

def by_value(item):
    return item[1]

max_profit_1 = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(profit_company.items(), key=by_value, reverse=True):     # O(n + n log n)
    if i < 3:                                                               # O(len(i))
        max_profit_1.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)

print(max_profit_1)                                                           # O(1)


# Cпособ №2:
# Сложность O (n**2)

max_profit_2 = {}                                           # O(1)

while len(max_profit_2) < 3:                                # O(n)
    max_value = 0                                           # O(1)
    for key, value in profit_company.items():               # O(n)
        if max_value < value:                               # O(len(i))
            max_value = value                               # O(1)
            key_max_value = key                             # O(1)
    max_value = profit_company.pop(key_max_value)           # O(1)
    max_profit_2.setdefault(key_max_value, max_value)       # O(1)

print(max_profit_2)                                         # O(1)

# Вывод: Первый способ выполняется быстрее так как самым "тяжелым" алгоритмом, является функция SORT() = O (n log n) линейно-логарифмическая,
# а во втором способе общая сложность О(n**2) квадратичная.