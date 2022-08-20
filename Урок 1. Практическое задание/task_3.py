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
company_dict = {
    'NVIDIA': 3491,
    'AMD': 2391,
    'Microsoft': 7823,
    'IBM': 4982,
    'Electronic Arts': 4211,
    'Amazon': 5338,
    'Sony': 6332,
    'McDonalds': 3899
}


def top3_1(dict):  # O(n log n) - общая

    income_list = sorted(dict.values())  # O(n log n)
    for key in dict.keys():  # O(n)
        if dict[key] == income_list[-1] or dict[key] == income_list[-2] or dict[key] == income_list[-3]:  # O(1)
            print(key)  # O(1)


#############################################################

def top3_2(dict):   # O(n) - общая
    max1 = dict['NVIDIA']     # O(1)
    max2 = dict['NVIDIA']     # O(1)
    max3 = dict['NVIDIA']     # O(1)
    for key in dict.keys():   # O(n)
        if dict[key] > max1:  # O(1)
            max3 = max2     # O(1)
            max2 = max1     # O(1)
            max1 = dict[key]    # O(1)
        if dict[key] > max2 and dict[key] < max1:   # 0(1)
            max3 = max2     # O(1)
            max2 = dict[key]    # O(1)
        if dict[key] > max3 and dict[key] < max2:   # O(1)
            max3 = dict[key]    # O(1)
    for key in dict.keys():  # O(n)
        if dict[key] == max1 or dict[key] == max2 or dict[key] == max3:  # O(1)
            print(key)  # O(1)


top3_1(company_dict)
print('--------------')
top3_2(company_dict)

# Вывод: 2-ое решение будет все эффективнее при возрастании размера входных данных,
# из-за более низкой итоговой сложности алгоритма.