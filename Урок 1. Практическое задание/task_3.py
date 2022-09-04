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
Выведите результат."""

<<<<<<< HEAD
сompany = {
    'hjkhj': 654,
    'hjghjghj': 78,
    'mlkk': 123,
    'jjnjnjk': 86,
    'mbnmnnn': 987,
    'mnnm': 768,
    'dfdfghj': 965,
    'lkjunjh': 456,
    'ilhigu': 876,
    'nlkn': 431,
    'jnnnnkk': 534,
    'nmmknn': 765
}

# первый вариант
def func1(company): #O(n*log n)
    sorted_company = sorted(company.items(), key=lambda x: x[1], reverse=True) #O(n*log n)
    print(dict(sorted_company[:3])) #O(n)

# второй вариант
def func2(company): #O(n)
    dict_sorted = {} #O(1)
    for i in range(3): #O(1)
        k = max(company, key=company.get) #O(n)
        dict_sorted[k] = company[k] #O(1)
        del company[k] #O(1)
    print(dict_sorted) #O(1)

func1(сompany)
func2(сompany)
=======
def func1(*args): #O(n)
    names_list = {} #O(1)
    for k, v in args: #O(n)
        names_list[k] = v #O(1)
        sorted_list = sorted(names_list.values())
    return names_list.get #O(1)

print(func2(1:7, 4, 8))
>>>>>>> lesson_1


"""
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

