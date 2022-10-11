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

def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
def random_value():
    return random.randint(100, 100000)

random_dict = {random_key(): random_value() for _ in range(10)}
print(random_dict)


#1. O(N^2)
for k, v in random_dict.items():                        # O(N)
    if v in sorted(list(random_dict.values()))[-3:]:    # O(N) + O(1) + O(len(random_dict) + 0(N*logN)
        print(k, "-", v)                                # O(1)

#2. O(N)
print((sorted(list(random_dict.items()), key=lambda x: x[1]))[-3:])     #  O(N) + O(len(random_dict) + 0(N*logN) + O(1)