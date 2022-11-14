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


from time import perf_counter

def pribl1(data): #сложность: O(N,logN) = O(N) + O(N,logN) + O(1) + O(N) * O(1) * O(1) + O(1)
    check = list(data.values())             # O(N)
    check.sort()                            # O(N,logN)
    bestComp = {}                           # O(1)
    for key, value in data.items():         # O(N)
        if value in check[-3:]:             # O(1)
            bestComp[key] = value           # O(1)
    return bestComp                         # O(1)



def pribl2(data):  #сложность: O(n log n)
    check = sorted(data.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    bestComp = dict(check[0:3]) #O(n)

    return bestComp  # O(1)

comp = {'Tesla': 4000, 'Apple': 3000, 'VTB': 1000, 'AMAZON': 3500, 'ENERGY': 1300}
start1 = perf_counter()
print(pribl1(comp), (perf_counter() - start1))
print("next")
start2 = perf_counter()
print(pribl2(comp), (perf_counter() - start2))
