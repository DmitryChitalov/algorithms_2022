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

profit_company = {'yandex': 100000, 'uber': 40000, 'maxim': 20000, 'gruz': 5000, 'get': 3000}
print(len(profit_company))

# Первый способ:
# сложность O(n log n)


def by_value(item):
    return item[1]                                                           # O(1)


max_profit = {}                                                              # O(1)
i = 0                                                                        # O(1)
for key, val in sorted(profit_company.items(), key=by_value, reverse=True):  # O(n + n log n)
    if i < 3:                                                                # O(1)
        max_profit.setdefault(key, val)                                      # O(1)
    i += 1                                                                   # O(1)
print(max_profit)                                                            # O(1)


# Второй способ:
# Сложность O (n**2)


max_profit_2 = {}                                                           # O(1)
while len(max_profit_2) < 3:                                                # O(n)
    max_value = 0                                                           # O(1)
    key_max_value = 0                                                       # O(1)
    for key, value in profit_company.items():                               # O(n)
        if max_value < value:                                               # O(len(max_value))
            max_value = value                                               # O(1)
            key_max_value = key                                             # O(1)
    profit_company.pop(key_max_value)                                       # O(1)
    max_profit_2.setdefault(key_max_value, max_value)                       # O(1)

print(max_profit_2)

"""
Вывод: Первый способ выполняется быстрее так как самым "тяжелым" алгоритмом,
является функция SORT() = O (n log n)
"""
