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

company = {
    'Saudi Aramco': 105369,
    'Alphabet': 76033,
    'Apple': 94680,
    'Microsoft': 61271,
    'Berkshire Hathaway': 89795
}

print('\nРешение №1: сложность O(n log n)\n')
company_sorted = sorted(company.items(), key=lambda item: item[1], reverse=True)  # O(n log n)
for i in range(3):  # O(1)
    print(f'Компания №{i + 1}: {company_sorted[i][0]}, прибыль {company_sorted[i][1]}')  # O(1) + O(1) = O(1)

print('\nРешение №2: сложность O(n^2)\n')
profit = list()
for key, value in company.items():  # O(n)
    profit.append(value)
for i in range(len(profit)):  # O(n^2) (квадратичная сложность потому что цикл в цикле)
    for j in range(len(profit)):
        if profit[i] > profit[j]:
            profit[i], profit[j] = profit[j], profit[i]
for i in range(3):  # O(n) (линейная сложность потому что в основной цикл вложен 'проход' по словарю)
    for key, value in company.items():
        if profit[i] == value:
            print(f'Компания №{i + 1}: {key}, прибыль {value}')