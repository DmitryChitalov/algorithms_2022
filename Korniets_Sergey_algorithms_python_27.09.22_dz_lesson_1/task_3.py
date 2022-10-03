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
import random
import string

# Создаем и заполняем хранилище
storage = {}
for x in range(30):
    name = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    profit = random.randint(1000, 10000000)
    storage[name] = profit

print(storage)

# Первый вариант решения
# Сложность: O(N log N)
max_profit_1 = dict(sorted(storage.items(), key=lambda item: item[1], reverse=True)[:3])     # O(N log N)
print('First method: ', max_profit_1)

# Второй вариант
# Сложность: O(n^2)
max_profit_2 = {}                                                                       # O(1)
for i in range(3):                                                                      # O(n)
    key_m = ''                                                                          # O(1)
    value_m = 0                                                                         # O(1)
    for key, value in storage.items():                                                  # O(n)
        if value > value_m:                                                             # O(1)
            value_m = value                                                             # O(1)
            key_m = key                                                                 # O(1)
    max_profit_2[key_m] = value_m                                                       # O(1)
    storage.pop(key_m)                                                                  # O(1)
print('Second method: ', max_profit_2)

"""
Вывод:
Первый вариант решения быстрее,и имеет меньшее количество строк кода
"""

