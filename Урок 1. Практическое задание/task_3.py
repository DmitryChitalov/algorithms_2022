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
import time


PROFIT_DICT = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500, 'F': 150, 'G': 250}
PROFIT_DICT_1 = {'100': 'A', '200': 'B', '300': 'C', '400': 'D', '500': 'E', '150': 'F', '250': 'G'}

# Сложность O(N) = O(3 * N)
start_time = time.clock()

for i in range(3):  # O(1)
    max_profit = 0  # O(1)
    name_company = ''  # O(1)

    for el in PROFIT_DICT.items():  # O(N)  /элемент это кортеж 0 - ключ, 1 - значение.
        if el[1] > max_profit:  # O(1)
            max_profit = el[1]  # O(1)
            name_company = el[0]  # O(1)
    print(f'Компания {name_company} - прибыль {max_profit}.')  # O(1)
    del PROFIT_DICT[name_company]  # O(1)

print("{:g} s".format(time.clock() - start_time))

# O(N * logN) = O(len(sorted_d)) + O(N * logN) + O(1)
start_time = time.clock()
sorted_d = dict(sorted(PROFIT_DICT_1.items(), key=lambda f: int(f[0])))  # O(N * logN) = O(len(N)) + O(N * logN)
#  сложность сортировки нашля для списка O(N * logN), взяла по анологии.
print(sorted_d)  # O(1)
my_max = sorted_d.popitem()  # O(1)
print(f'Компания {my_max[1]} - прибыль {my_max[0]}.')  # O(1)
my_max = sorted_d.popitem()  # O(1)
print(f'Компания {my_max[1]} - прибыль {my_max[0]}.')  # O(1)
my_max = sorted_d.popitem()  # O(1)
print(f'Компания {my_max[1]} - прибыль {my_max[0]}.')  # O(1)
print("{:g} s".format(time.clock() - start_time))
# Алгоритм со сложностью O(N) эффективнее, чем со сложностью O(N * logN).
