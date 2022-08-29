"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""


profit_company = {'Nike': 1000, 'Adidas': 4000, 'Puma': 2000, 'TH': 5000, 'UA': 3000}
print(len(profit_company))

# Первый способ:
# сложность O(n log n)


def by_value(item):
    return item[1]                                                          # O(1)


max_profit = {}                                                             # O(1)
i = 0                                                                       # O(1)
for k, v in sorted(profit_company.items(), key=by_value, reverse=True):     # O(n + n log n)
    if i < 3:                                                               # O(len(i)
        max_profit.setdefault(k, v)                                         # O(1)
    i = i + 1                                                               # O(1)
print(max_profit)                                                           # O(1)


# Второй способ:
# Сложность O (n**2)

global max_value                                                            # O(1)
global key_max_value                                                        # O(1)

max_profit_2 = {}                                                           # O(1)
while len(max_profit_2) < 3:                                                # O(n)
    max_value = 0                                                           # O(1)
    for key, value in profit_company.items():                               # O(n)
        if max_value < value:                                               # O(len(max_value))
            max_value = value                                               # O(1)
            key_max_value = key                                             # O(1)
    max_value = profit_company.pop(key_max_value)                           # O(1)
    max_profit_2.setdefault(key_max_value, max_value)                       # O(1)

print(max_profit_2)

# Вывод: Первый способ выполняется быстрее так как самым "тяжелым" алгоритмом,
# является функция SORT() = O (n log n)