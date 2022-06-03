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

# Заполнение массива тестовыми данными
company_storage = []
for x in range(50):
    company_storage.append({
        'name': ''.join(random.choice('vxnxikmhdc') for i in range(32)),
        'income': random.randint(893945, 93277238)
    })


# print(company_storage)


# Реализуйте поиск трех компаний с наибольшей годовой прибылью.

# O(N log N)
def first_method(in_storage):
    # gen_new_list = list(map(lambda x: (x[1]['income'], x[0]), enum)) # O(n)?
    gen_new_list = []
    for idx, x in enumerate(in_storage):  # O(n)
        gen_new_list.append((x['income'], idx))  # O(1)
    gen_new_list.sort(reverse=True)  # O(N log N)
    return [in_storage[i] for i in map(lambda x: x[1], gen_new_list[:3])]  # O(3)


# O(N log N)
def two_method(in_storage: list) -> list:
    """ Вернуть 3 наибольших годовых прибылей (компании) """
    in_storage.sort(key=lambda x: x['income'], reverse=True)  # O(N log N)
    return in_storage[:3]  # O(3-0)


# O (n^2)
def three_method(in_storage):
    result = in_storage[0:3] # O(3)
    for x in in_storage:  # O(n)
        minimal = None # O(1)
        to_change = None # O(1)
        for idx, min in enumerate(result):  # O(n)
            if minimal is None: # O(1)
                minimal = min['income'] # O(1)
            else: # O(1)
                if min['income'] < minimal: # O(1)
                    to_change = idx # O(1)
        if x['income'] > result[to_change]['income']: # O(1)
            result[to_change] = x # O(1)
    return result


print(f"first_method: {first_method(company_storage)}")
print(f"two_method: {two_method(company_storage)}")
print(f"three_method: {three_method(company_storage)}")

"""

Вывод: 

Второй лучше всего, сложность меньше, кол-во операций, и по памяти используем уже созданную область.
А также есть комментарий функции, и указаны типы.

Самый худший и имеет неверные результаты - третий способ.
Первый имеет нормальные результаты, но всё также плох.

"""
